##################
#PreProcesamiento#
##################


### Cargar paquetes
library(tm)


### Abrir/Cargar los datos
drel_data <- read.csv("DeathRowExecutedLast_preproc.csv", header=TRUE, encoding="UTF-8" )


### Transformaciones sobre columna last_words

# Crear corpus(last_words)
corpusLW <- Corpus(VectorSource(drel_data$last_words))
# Eliminar caracteres de puntuacion
corpusLW <- tm_map(corpusLW, removePunctuation)
# Eliminar caracteres numericos
corpusLW <- tm_map(corpusLW, removeNumbers)
# Convertir caracteres alfabeticos a minusculas
corpusLW <- tm_map(corpusLW, tolower)
# Crear vector de stopwords a eliminar
#LWdtm <- TermDocumentMatrix(corpusLW, control=list(minWordLength=1))
#findFreqTerms(LWdtm, lowfreq = 30)
myStopWords <- c(stopwords('english'), "none", "english", "spanish", "written", "statement")
# Eliminar stopwords
corpusLW <- tm_map(corpusLW, removeWords, myStopWords)
# Eliminar espacios en blanco extra
corpusLW <- tm_map(corpusLW, stripWhitespace)
# Actualizar columna(last_words) en dataset
drel_data$last_words <- sapply(corpusLW, as.character)


### Transformaciones sobre columna race

# Crear corpus(race)
corpusR <- Corpus(VectorSource(drel_data$race))
# Convertir caracteres alfabeticos a minusculas
corpusR <- tm_map(corpusR, tolower)
# Eliminar espacios en blanco extra
corpusR <- tm_map(corpusR, stripWhitespace)
# Actualizar columna(race) en dataset
drel_data$race <- sapply(corpusR, as.factor)


### Transformaciones sobre columna county

# Crear corpus(county)
corpusC <- Corpus(VectorSource(drel_data$county))
# Convertir caracteres alfabeticos a minusculas
corpusC <- tm_map(corpusC, tolower)
# Eliminar espacios en blanco extra
corpusC <- tm_map(corpusC, stripWhitespace)
# Actualizar columna(county) en dataset
drel_data$county <- sapply(corpusC, as.factor)


### Cambiar formato columna(date) 
drel_data$date <- as.Date(drel_data$date, "%m/%d/%Y")


### New data_postproc
vminable <- data.frame("last_words" = drel_data$last_words,
                       "age" = drel_data$age,
                       "date" = drel_data$date,
                       "race" = drel_data$race,
                       "county" = drel_data$county)


### Exportar
write.csv(vminable, file="lastWords_dataset.csv", row.names=FALSE, na="")

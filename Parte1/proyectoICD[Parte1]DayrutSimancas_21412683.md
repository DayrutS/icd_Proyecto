# Proyecto: Parte 1 _ Introduccion a la Ciencia de Datos

## _Dayrut Simancas CI: 21412683_

### **Antecedentes y motivacion:**

A lo largo de nuestras vidas vivimos grandes cantidades de primeros momentos, entre ellos uno de los mas significantes son nuestras primeras palabras; momento marcado y recordado por todos aquellos que logran ser testigos de ellas. Por el otro lado, las ultimas palabras de una persona son raramente recordadas y menos comun aun son registradas.

Desde 1976 en los Estados Unidos, 1447 personas(hombres y mujeres) han sido sancionadas y ejecutadas bajo pena de muerte(capital punishment / death penalty). De estas ejecuciones, al menos un tercio han sido realizadas en el estado de Texas, e interesantemente el Texas Department of Criminal Justice aloja un repositorio de las ultimas palabras habladas por cada preso antes de ser llevada acabo su sentencia.

A lo largo del curso de la materia, se han ido mencionando ejemplos de distantas aplicaciones/actividades que pueden ser realizadas gracias a la ciencia de datos, entre ellas una de las que mas me llamo la atencion fue el 'analisis de sentimientos' de tweets hecho por personas dentro de la red social sobre ciertos topicos, o tambien 'sentiment analysis' de los reviews hecho por clientes sobre productos de una empresa. Por lo que este proyecto es una oportunidad para ampliar conocimientos sobre dicho topico.

### **Objetivos del proyecto:**

Emplear tecnicas de NLP (natural language processing) y de analisis de textos (text analysis/mining) para tratar de determinar el estado emocional de los presos sentenciados a muerte durante sus ultimos momentos. Y tratar de responder preguntas como:

+ ¿Cuales son las emociones predominantes exhibidas por alguien bajo este tipo de situacion en particular? Tristeza? Arrepentimiento? Ira?

+ ¿En que estan pensando los sentenciados durante sus ultimos momentos?

+ ¿La edad o raza de la persona influyen de alguna manera?


### **Fuente(s) de datos:**

La data sera extraida de la pagina del [Texas Department of Criminal Justice](http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html)

+ La cual detalla en sus columnas:
    - Execution: numero de ejecucion
    - Link: informacion extra sobre la persona ejecutada
    - link: ultimas palabras del sentenciado
    - Last name: apellido
    - First name: nombre
    - TDCJ number: id dentro del Texas Department Criminal Justice
    - Age: edad
    - Date: fecha de ejecucion
    - Race: raza
    - County

### **Vision general del disenio:**

1) Scraping_Coleccion de la Data: emplear metodos de web scraping para recolectar los datos de la pagina web.

2) Preprocesamiento de la data: limpieza, transformacion y preparacion de los datos.

3) Explorar Data: sumarizar caracteristicas principales del dataset.

4) Analisis de Datos(Sentiment Analysis):

5) Visualizacion: presentar los resultados.

### **Verificacion. ¿Como verificara el estado de exito de su proyecto?:**

Las emociones identificadas servirian como un parametro de clasificacion(class label) para los registros, por lo que se podria subdividir la data en training/test set, y basandonos en un modelo predictivo verificar que tan preciso resulta el modelo.

### **¿Como visualizara y presentara los resultados?:**

Los resultados/informacion podrian ser presentados usando un conjunto de graficos de barra, torta, wordclouds, etc; todos estos agrupados en un solo archivo informe de documentacion y/o infoposter con los datos e informaciones mas relevantes. 

### **Cronograma en terminos semanales:**

- 17 de marzo(viernes)_fecha entrega de la parte1 del proyecto
- 21 de abril(viernes)_fecha de entrega de la parte2 del proyecto
- 5 semanas de una fecha a la otra

Basandonos en la vision general de disenio indicada anteriormente, podemos asignar una semana para cada una de las fases/actividades a realizar; lo cual (idealmente) determina el siguiente plan de trabajo:

1) semana del 24 de marzo(viernes) para realizar el web scraping/recoleccion de los datos

2) semana del 31 de marzo(viernes) para realizar la limpieza y preparacion de los datos

3) semana del 7 de abril(viernes) para analisis exploratorio de los datos

4) semana del 14 de abril(viernes) para realizar el analisis de sentimiento sobre los datos

5) semana del 24 de abril(viernes) para preparar los documentos finales de entrega del proyecto
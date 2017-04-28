# Proyecto: Parte 2 _ Introduccion a la Ciencia de Datos

## _Dayrut Simancas CI: 21412683_

### **Introduccion y Motivacion**

A lo largo de nuestras vidas vivimos grandes cantidades de primeros momentos, entre ellos uno de los mas significantes son nuestras primeras palabras; momento marcado y recordado por todos aquellos que logran ser testigos de ellas. Por el otro lado, las ultimas palabras de una persona son raramente recordadas y menos comun aun son registradas.

Desde 1976 en los Estados Unidos, 1447 personas(hombres y mujeres) han sido sancionadas y ejecutadas bajo pena de muerte(capital punishment / death penalty). De estas ejecuciones, al menos un tercio han sido realizadas en el estado de Texas, e interesantemente el Texas Department of Criminal Justice aloja un repositorio de las ultimas palabras habladas por cada preso antes de ser llevada acabo su sentencia.

El _objetivo principal_ de este proyecto fue el de emplear tecnicas de NLP (natural language processing) y de analisis de textos (text analysis/mining) para tratar de determinar el estado emocional de los presos sentenciados a muerte durante sus ultimos momentos.

### **Antecedentes**

A lo largo del curso de la materia, se fueron mencionando ejemplos de distantas aplicaciones/actividades que pueden ser realizadas gracias a la ciencia de datos, entre ellas una de las que mas me llamo la atencion fue el 'analisis de sentimientos' de tweets hecho por personas dentro de la red social sobre ciertos topicos, o tambien 'sentiment analysis' de los reviews hecho por clientes sobre productos de una empresa. Por lo que este proyecto resulto ser una oportunidad para ampliar conocimientos sobre dicho tema.

Pero la idea original de realizar un analisis de sentimientos, especificamente sobre el dataset utilizado, proviene de un [articulo en la web](http://rs.io/100-interesting-data-sets-for-statistics) donde hacen mencion de 100+ datasets(de distintos topicos, areas de enfoque y tematicas variadas) los cuales podrian resultar interesantes para personas/estadisticos; con el objetivo de realizar algun tipo de trabajo, investigacion, o por simple curiosidad.

### **Preguntas Iniciales**

Inicialmente las preguntas principales que se trataron de responder fueron:

+ ¿Cuales son las emociones predominantes exhibidas por alguien bajo este tipo de situacion en particular? Tristeza? Arrepentimiento? Ira?

+ ¿En que estan pensando los sentenciados durante sus ultimos momentos?

Posterior a la realizacion del analisis de sentimientos surgieron interrogantes tales como:

+ ¿Por que la emocion 'joy'/'alegria' es tan predominante en los resultados obtenidos? (motivos de las bajas frecuencias de otros tonos emocionales)

+ ¿De donde provienen los tetragramas mas frecuentes? (dificil de proporcionar un contexto a las frases dichas)

### **Datos**

#### _Datos - Fuente de Datos_

La fuente de datos proviene de la pagina del [Texas Department of Criminal Justice](http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html).

El dataset extraido detalla en sus columnas la siguiente informacion: 

- Execution: numero de ejecucion
- Link: informacion extra sobre la persona ejecutada
- link: ultimas palabras del sentenciado
- Last name: apellido
- First name: nombre
- TDCJ number: id dentro del Texas Department Criminal Justice
- Age: edad
- Date: fecha de ejecucion
- Race: raza
- County: condado del estado de Texas

#### _Datos - Web Scraping_

El web scraping se realizo mediante el uso de un script escrito en lenguaje Python (.py). Dicho script inicialmente obtiene la estructura de la pagina (HTML tree), luego busca en el codigo html los elementos &lt;tr&gt; correspondientes a las filas de la tabla que se desea extraer. Y posteriormente para cada fila (&lt;tr&gt;) se buscan los elementos &lt;td&gt; (las casillas de la tabla) donde se encuentran los datos de interes. De las casillas de la primera fila se obtuvieron los encabezados/nombres de las columnas, y de las casillas del resto de la tabla se extrayeron las observaciones/muestras.

Las casillas de la columna correspondiente a las ultimas palabras de los ejecutados 'last_statement' eran un conjunto de links (uno para cada convicto ejecutado) los cuales redireccionaban a otra pagina donde se encontraban los datos principales que se buscaban. Por lo que se realizo un proceso similar al descrito anteriormente, con la diferencia de que esta vez se busco dentro del codigo de la pagina correspondiente a cada convicto, el elemento identificado como 'body' y dentro del mismo se busco especificamente por aquel elemento  &lt;p&gt; (parrafo de texto); cuya clase era 'text_bold' AND empezaba con las palabras 'last statement'. Con esto el proceso de scripting culmina, y los datos extraidos son exportados a un archivo .csv (comma separated value) para su futuro uso.

#### _Datos - Preprocesamiento_

El proceso de limpieza del dataset, se puede subdivir en distintos pasos:

0. _Eliminacion de ciertos caracteres especiales:_ Ya que los datos fueron extraidos de paginas html, al momento de cargarlos del .csv generado y tratarlos como puro texto de codificacion utf-8 en Rstudio, habia ciertos caracteres especiales que dificultaban la lectura y operaciones sobre ciertos campos. Variaciones de comillas simples ('') y dobles (""), especialmente cuando aparecian intercaladas en textos delimitados por las mismas.

1. _Completacion de datos faltantes:_ Hubo ciertas casillas bajo la columna de ultimas palabras 'last_words' cuyos valores no fueron obtenidos, debido a que estos venian encasilladas bajo otro tipo de estructura al esperado dentro de la paginas. Por lo que manualmente estos datos faltantes fueron agregados a sus filas correspondientes.

2. _Eliminacion de caracteres de puntuacion:_ comas, puntos, parentesis, signos de interrogacion, etc.; sin estos caracteres se logra un mejor nivel de claridad y separacion entre las palabras de los textos, ademas de que para ciertas actividades de mineria de texto resultan ser innecesarios.

3. _Eliminacion de caracteres numericos:_ 0 .. 9; estos caracteres no suelen ofrecer informacion util para el analisis de textos, y no se ve su importancia cuando el objetivo es realizar analisis de sentimientos.

4. _Conversion de caracteres alfabeticos a minusculas:_ para obtener uniformidad en la data a analizar y facilitar la identificacion de terminos comunes en la data, palabras que pudieron haber estado escritos de distinta manera pero ofrecen la misma informacion (ejm: 'word', 'Word', 'WORD').

5. _Eliminacion de palabras no informativas (stopwords):_ una de las operaciones mas importantes, ya que se reduce la dimensionalidad de los textos a analizar. Articulos, preposiciones, pronombres, etc.; son palabras esenciales para darle sentido a los lenguajes escritos y hablados pero al momento de realizar mineria de texto podrian alterar/influenciar los resultados obtenidos por su alta frecuencia e informacion poco relevante bajo ciertos contextos.

6. _Eliminacion de espacios en blanco extra:_ simplemente se contraen multiples caracteres consecutivos como [ \s \t \n \r ] en uno solo, para visualmente y en memoria reducir el espacio requerido para representar los textos.

7. _Reducir dimensionalidad de la data por columnas:_ se eliminaron del dataset todas aquellas columnas que fueron consideradas pocos relevantes al momento de realizar sentimiento de analisis.

### **Analisis Exploratorio**

Fueron extraidos en total 542 perfiles de convictos ejecutados. De los cuales solo 428 optaron por decir sus ultimas palabras (114 ejecutados se negaron de una u otra manera).

La edad promedio de los convictos ejecutados fue de 38 anios. Siendo los mas jovenes 24, y el mas viejo 67.

La proporcion de las razas de los ejecutados fue: 44.46% 'white'/blancos, 36.35% 'black'/negros, 18.82% 'hispanic'/hispanos, 0.37% 'other'/otra raza.

1982 fue el anio con menor cantidad de ejecuciones solo 1_una (primer anio registrado en el dataset). Mientras que el anio con mayor numero de ejecuciones fue el 2000 40_ejecuciones; posterior a esta fecha la cantidad de convictos ejecutados anuales ha venido en declive.

**_¿En que estan pensando/de que hablan los sentenciados durante sus ultimos momentos?_**

Para determinar cuales eran los temas/topicos que los convictos hacian mas referencia durante sus ultimas palabras, se utilizo una combinacion de nubes de palabras y graficos de barras de las palabras, los bigramas, los trigramas y los tetragramas mas frecuentes. Los bi-tri-tetra/gramas fueron incluidos para poder darle contexto a las palabras que por si solas significan una cosa pero cuando aparecen combinadas con otras pueden tener un significado totalmente distinto. Con todo esto en consideracion, se llego a la conclusion de que los convictos en sus ultimos momentos:

* Le dicen a sus familiares que los aman (personalmente si se encuentran alli; o por medio de terceros en caso de familia no presente)

* Ofrecen mensajes alentadores a personas queridas (frases como 'stay strong' y 'take care')

* Ofrecen disculpas a las familias de sus victimas (frases predominantes: 'im sorry', 'sorry pain caused')

* Rezan o hacen referencias religiosas (la mayoria de los tetragramas hacian referencias a versos de la Biblia o eran parte de Lord’s Prayer)

**_¿Cuales son las emociones predominantes exhibidas por los sentenciados?_**

la mayoria de las 'ultimas palabras' presentaban una tonalidad/polaridad positiva. Expresando amor por sus familiares, mensajes alentadores, disculpas, religion y hasta gratitud.

Mientras que las 'ultimas palabras' de tono negativo expresaban arrepentimiento, disculpas y hasta algunas declaraciones de inocencia. La poca cantidad de expresiones negativas por parte de los ejecutados hace pensar que el sistema penitenciario es exitoso rehabilitando a sus convictos; o el simple hecho de que los convictos, por estar en el tipo de ambiente que las prisiones ofrecen, se ven atraidos a las practicas religiosas (religion parece ser un tema asociado con emociones positivas dentro de herramientas NLP).

### **Analisis Final**

Las 'ultimas palabras' de los ejecutados en su gran mayoria fueron clasificadas bajo la emocion 'joy'/alegria. Lo que podria prestarse a malinterpretaciones; debido a que luego de examinar con un poco mas de atencion las 'ultimas palabras' bajo esta categoria nos podemos dar cuenta de que se podria estar presentandose una miscategorizacion a causa de la alta frecuencia de "expresiones de amor" y expresiones religiosas. Frases como: ['love yall', 'family love', 'god bless', 'jesus christ', 'know love'] podrian ser los causantes de los resultados obtenidos.

### **Referencias**

- Robb Seaton. "100+ Interesting Data Sets for Statistics". http://rs.io/100-interesting-data-sets-for-statistics

- Texas Department of Criminal Justice. http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html

- gramener_scraper. https://github.com/gramener/texas-deathrow

- Thierry Gregorius. "How I used R to create a word cloud, step by step". https://georeferenced.wordpress.com/2013/01/15/rwordcloud/

- Brian Zive. "Text Mining and N-Grams". https://rpubs.com/brianzive/textmining

- Reuben Kearney. "UPDATED: Sentiment Analysis with 'sentiment'". https://reubenkearney.com/2015/06/07/updated-sentiment-analysis-with-sentiment/


# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<22\>/\<23\>)
Autor/a: \<Javier Pallarés González\>   uvus:\<javpalgon/MGF6851\>

El objetivo de este proyecto es analizar y estudiar los datos y características de los shows más famosos de la televisión, publicados en el dataset de Kaggle(https://www.kaggle.com/datasets/ruchi798/tv-shows-on-netflix-prime-video-hulu-and-disney). Este dataset constaba de 12 columnas, pero ninguna de tipo fecha, por lo tanto, hemos generado una columna de fechas aleatorias correspondiéndose con la fecha de estreno de estos programas de TV. Por último hemos eliminado 4 columnas, lo que supondrá un total de 9 columnas.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<proyecto.py\>**: En este módulo se encuentra la función que lee los datos del .csv y los inserta en una lista vacía de manera ordenada.
  * **\<test_proyecto.py\>**: En el módulo de pruebas se invocan las funciones del módulo proyecto.py, ya que aquí se encuentra el main. 
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<TV_SHOWS_0.csv\>**: Fichero donde se encuentran todos los datos con los que hemos trabajado.

    
## Estructura del *dataset*

El dataset está compuesto por \<9\> columnas, con la siguiente descripción:

* **\<ID>**: de tipo \<int\>, es un identificador entero
* **\<Title>**: de tipo \<str\>, es una cadena de caracteres donde se encuentran los títulos de los shows
* **\<Age>**: de tipo \<str\>, representa una cadena de caracteres. Indica la edad mínima para poder ver la serie
* **\<rating>**: de tipo \<float\>, representa la valoración de la serie sobre 10.
* **\<Netflix>**: de tipo \<boolean\>, indica si el show se retransmite en Netflix o no.
* **\<Hulu>**: de tipo \<boolean\>, indica si el show se retransmite en Hulu o no.
* **\<Prime_Video>**: de tipo \<boolean\>, indica si el show se retransmite en Prime_Video o no.
* **\<Disney+>**: de tipo \<boolean\>, indica si el show se retransmite en Disney+ o no.
* **\<release_date>**: de tipo \<date\>, representa la fecha cuando se estrenó la serie. Esta columna fue generada mediante datos aleatorios.

## Tipos implementados

Se ha utilizado la siguiente tupla con nombre:
tvshows=namedtuple('TvShows', 'ID, Title, Age, rating, Netflix, Hulu, Prime_Video, Disney_Plus, Release_Date')

Los tipos de cada uno de los campos son los siguientes:
tvshows(int, str, str, float, boolean, boolean, boolean, boolean, datetime.date)

## Funciones implementadas
Añade aquí descripciones genéricas de las funciones, que luego debes acompañar con comentarios de tipo documentación en el código

### \<modulo 1\>

* **<funcion 1>**: Descripción de la función 1.
* **<funcion 2>**: Descripción de la función 2.
* ...

### \<test modulo 1\>

* **<test funcion 1>**: Descripción de las pruebas realizadas a la función 1.
* **<test funcion 2>**: Descripción de las pruebas realizadas a la función 2.
* ...
* 
### \<modulo 2\>

* **<funcion 1>**: Descripción de la función 1.
* **<funcion 2>**: Descripción de la función 2.
* ...

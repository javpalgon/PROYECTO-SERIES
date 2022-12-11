# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<22\>/\<23\>)
Autor/a: \<Javier Pallarés González\>   uvus:\<javpalgon/MGF6851\>

El objetivo de este proyecto es analizar y estudiar los datos y características de los shows más famosos de la televisión, publicados en el dataset de Kaggle(https://www.kaggle.com/datasets/ruchi798/tv-shows-on-netflix-prime-video-hulu-and-disney). Este dataset constaba de 12 columnas, pero ninguna de tipo fecha, por lo tanto, hemos generado una columna de fechas aleatorias correspondiéndose con la fecha de estreno de estos programas de TV. Por último hemos eliminado 4 columnas, lo que supondrá un total de 9 columnas.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<proyecto.py\>**: En este módulo se encuentra la función que lee los datos del .csv y los inserta en una lista vacía de manera ordenada.
  * **\<test_proyecto.py\>**: En el módulo de pruebas se invocan las funciones del módulo proyecto.py, ya que aquí se encuentra el main. 
  * **\<grafica.py\>**: módulo creado únicamente para la gráfica y la función auxiliar.
  * **\<parsers.py\>**: módulo creado para parsear los boolean.
* **/data**: Contiene el dataset o datasets del proyecto.
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
Hemos implementado varias funciones que realizan diferentes tareas, situadas en los dos módulos de manera organizada. El módulo principal es proyecto.py

### \<modulo_proyecto\>

  * **<ENTREGA 1>**

* **<lee_datos(series)>**: Lee todos los datos del csv, devolviendo una lista de tuplas con los datos leídos.

  * **<ENTREGA 2>**
    * **<BLOQUE 1>**
* **<series_para_todos(series)>**: dadas una lista de tuplas de tipo info, nos devuelve una lista la cual contiene los nombres de todos los shows que no tienen edad mínima para ver.

* **<valoracion_media_netflix(series)>**: dadas una lista de tuplas de tipo info, almacena en una lista de tuplas todas las valoraciones de todos los shows que se pueden ver en Netflix.

    * **<BLOQUE 2>**
* **<valoraciones(series)>**: recibe una lista de tuplas de tipo info y nos devuelve una lista de tuplas que contiene las valoraciones de todas las series
* **<max_valoracion_series_familiares(series)>**: recibe una lista de tuplas de tipo info y devuelve la serie mejor valorada de tipo familiar.

* **<agrupar_segun_fecha_lanzamiento(series)>**: recibe una lista de tuplas y devuelve un diccionario con las series que han salido en el mismo año. Luego la clave es el año de lanzamiento y sus valores asociados son los shows que salieron en ese año.

  * **<ENTREGA 3>**
    * **<BLOQUE 3>** 
* **<total_series_por_anyo(series)>**: recibe una lista de tuplas y devuelve un diccionario cuyas claves son los anyos de lanzamiento de los shows y el valor de cada clave corresponde con el número de series que se lanzaron ese anyo.

* **<maximo_minimo_shows_por_anyo(series)>**: recibe el diccionario de la función anterior y devuelve dos tuplas, que corresponden al anyo donde más shows se publicaron y dónde menos.

* **<valoraciones_shows_por_edad(series,edad)>**: esta función sirve de apoyo para formar las 2 siguientes, ya que devuelve un diccionario cuyas claves son las edades recomendadas para ver el show y los valores son el título del show y su valoración correspondiente.

* **<mejor_serie_por_edad(series)>**: recibe el diccionario creado en la función anterior, y devuelve el titulo de la serie mejor valorada para cada edad recomendada, con su respectiva valoración.

* **<mejores_series_por_edad(series,n=3)>**: recibe el diccionario creado en 'valoraciones_shows_por_edad' y un entero n y devuelve las n series con mejor valoración para cada edad recomendada. Las claves siguen siendo la edad recomendada.

* **<top_series_ninyos_Disney_Plus(series,n=5)>**: recibe una lista de tuplas y un número entero n y devuelve una lista con n tuplas ordenadas de mayor a menor según su valoración. Estas series tienen que estar disponibles en Disney_Plus.

### \<modulo_grafica\>


  * **<BLOQUE 4>**
* **<total_series_segun_edad(series)>**: recibe una lista de tuplas y devuelve un diccionario cuyas claves son la edad para ver el show y cuyo valor, el número de series que hay para cada edad. Esta función es auxiliar para crear la gráfica.

* **<grafica_numero_series_segun_edad(series)>**: recibe el diccionario creado en la función anterior y devuelve una gráfica con el número total de shows que pertenecen a cada edad recomendada. 

### \<modulo_parsers\>
* **<parsea_bool(cadena)>**: dado un entero (en este caso, 1 o 0), devuelve 'True' si recibe un 1 y 'False' si recibe un 0. Esta función ha sido utilizada para leer los datos del csv en 'lee_datos'.


### \<modulo_test_proyecto\>

Aquí se ponen a prueba todas las funciones desarrolladas en el otro módulo, nombradas de igual manera pero con "test" delante. Por ejemplo:
* **<test_lee_datos(datos)>**
* **<test_series_para_todos(datos)>**
* **<test_valoracion_media_netflix(datos)>**
* **<test_max_valoracion_series_familiares(datos)>**
* **<test_agrupar_segun_fecha_lanzamiento(datos)>**
* **<test_total_series_por_anyo(datos)>**
* **<test_maximo_minimo_shows_por_anyo(datos)>**
* **<test_mejor_serie_por_edad(datos)>**
* **<test_mejores_series_por_edad(datos)>**
* **<test_top_series_ninyos_Disney_Plus(datos)>**
* **<test_grafica_numero_series_segun_edad(datos)>**





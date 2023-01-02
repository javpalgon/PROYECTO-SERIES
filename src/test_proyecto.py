from proyecto import *
from grafica import *

def test_lee_datos(datos):
    print(datos[0]) 
    print(datos[1])
    print(datos[2]) 
    
    print(datos[-1]) 
    print(datos[-2])
    print(datos[-3])
    
def test_series_para_todos(datos):
    print("Series para todos!: ",series_para_todos(datos), end=' ')

def test_valoracion_media_netflix(datos):
    print("valoracion media de los shows de netflix:", "{0:.2f}".format(valoracion_media_netflix(datos)))

def test_max_valoracion_series_familiares(datos):
    print("Te recomendamos esta serie para ver junto a los mas peques de casa!!:", max_valoracion_series_familiares(datos))

def test_agrupar_segun_fecha_lanzamiento(datos):
    numero_lanz= agrupar_segun_fecha_lanzamiento(datos)
    for i in numero_lanz.keys():
        print(" \t{} : {} ".format(i, numero_lanz[i]))

def test_total_series_por_anyo(datos):
    print("El número de shows que se publicaron por anyo es el siguiente:", total_series_por_anyo(datos))

def test_maximo_minimo_shows_por_anyo(datos):
    maximo, minimo = maximo_minimo_shows_por_anyo(datos)
    print("El anyo donde más shows se publicaron fue: ", maximo, " y el mínimo: ", minimo)

def test_mejor_serie_por_edad(datos):
    print("La mejor serie para cada edad recomendada es la siguiente:", mejor_serie_por_edad(datos))

def test_mejores_series_por_edad(datos):
    print("Top 3 series por cada edad", mejores_series_por_edad(datos, 5))

def test_top_series_ninyos_Disney_Plus(datos):
    print("Las mejores series de adultos que se pueden ver por Hulu: ", top_series_ninyos_Disney_Plus(datos, 2))

def test_total_series_segun_edad(datos):
    print(total_series_segun_edad(datos))

def test_grafica_numero_series_segun_edad(datos):
    print(grafica_numero_series_segun_edad(datos))

def main():
    tv_series = lee_datos("./data/TV_SHOWS_0.csv")
    print("Entrega 1-------------------------------------------------------")
    test_lee_datos(tv_series)
    print("Entrega 2-------------------------------------------------------")
    test_series_para_todos(tv_series)
    print("----------------------------------------------------------------")
    test_valoracion_media_netflix(tv_series)
    print("----------------------------------------------------------------")
    test_max_valoracion_series_familiares(tv_series)
    print("----------------------------------------------------------------")
    test_agrupar_segun_fecha_lanzamiento(tv_series)
    print("Entrega 3-------------------------------------------------------")
    test_total_series_por_anyo(tv_series)
    print("----------------------------------------------------------------")
    test_maximo_minimo_shows_por_anyo(tv_series)
    print("----------------------------------------------------------------")
    test_mejor_serie_por_edad(tv_series)
    print("----------------------------------------------------------------")
    test_mejores_series_por_edad(tv_series)
    print("----------------------------------------------------------------")
    test_top_series_ninyos_Disney_Plus(tv_series)
    print("----------------------------------------------------------------")
    test_total_series_segun_edad(tv_series)
    print("----------------------------------------------------------------")
    test_grafica_numero_series_segun_edad(tv_series)

if __name__ == "__main__":
    main()
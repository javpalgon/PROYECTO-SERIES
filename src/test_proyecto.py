from proyecto import *
def test_series_para_todos(lee_datos):
    print("Series para todos!: ",series_para_todos(lee_datos), end=' ')

def test_valoracion_media_netflix(series_netflix):
    calculo_media = valoracion_media_netflix(series_netflix)
    media= (sum(calculo_media)/len(calculo_media))
    print("valoracion media de los shows de netflix:", "{0:.2f}".format(media))

def test_max_valoracion_series_familiares(valoraciones):
    print("Te recomendamos esta serie para ver junto a los mas peques de casa!!:", max_valoracion_series_familiares(valoraciones))

def test_agrupar_segun_fecha_lanzamiento(lee_datos):
    numero_lanz= agrupar_segun_fecha_lanzamiento(lee_datos)
    for i in numero_lanz.keys():
        print(" \t{} : {} ".format(i, numero_lanz[i]))

def main():
    tv_series = lee_datos("./data/TV_SHOWS_0.csv")

    #print(tv_series) 
    #print(tv_series[1])
    #print(tv_series[2]) 
    
    #print(tv_series[-1]) 
    #print(tv_series[-2])
    #print(tv_series[-3])
    test_series_para_todos(tv_series)
    #test_valoracion_media_netflix(tv_series)
    #test_max_valoracion_series_familiares(tv_series)
    #test_agrupar_segun_fecha_lanzamiento(tv_series)

if __name__ == "__main__":
    main()
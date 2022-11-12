from proyecto import *
def test_filtra_por_edad(proyecto):
    print("Series +18: ",filtra_por_edad(proyecto), end=' ')

def test_valoracion_media_netflix(proyecto):
    calculo_media = valoracion_media_netflix(proyecto)
    media= (sum(calculo_media)/len(calculo_media))
    print("valoracion media de los shows de netflix:", "{0:.2f}".format(media))

def test_max_valoracion_series_familiares(proyecto):
    print("Te recomendamos esta serie para ver junto a los mas peques de casa!!:", max_valoracion_series_familiares(proyecto))

def test_agrupar_segun_fecha_lanzamiento(proyecto):
    numero_lanz= agrupar_segun_fecha_lanzamiento(proyecto)
    for i in numero_lanz.keys():
        print("\t{}: {}".format(i, numero_lanz[i]))

def main():
    tv_series = lee_datos("./data/TV_SHOWS_0.csv")

    #print(tv_series) 
    #print(tv_series[1])
    #print(tv_series[2]) 
    
    #print(tv_series[-1]) 
    #print(tv_series[-2])
    #print(tv_series[-3])
    #test_filtra_por_edad(tv_series)
    #test_valoracion_media_netflix(tv_series)
    #test_max_valoracion_series_familiares(tv_series)
    test_agrupar_segun_fecha_lanzamiento(tv_series)

if __name__ == "__main__":
    main()
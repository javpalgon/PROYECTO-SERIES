from proyecto import *
def test_filtra_por_edad(proyecto):
    print("Series +18: ",filtra_por_edad(proyecto), end=' ')

def test_valoracion_media_netflix(proyecto):
    calculo_media = valoracion_media_netflix(proyecto)
    media= (sum(calculo_media)/len(calculo_media))
    print("valoracion media de los shows de netflix:", "{0:.2f}".format(media))

def main():
    tv_series = lee_datos("./data/TV_SHOWS_0.csv")

    #print(tv_series[0]) 
    #print(tv_series[1])
    #print(tv_series[2]) 
    
    #print(tv_series[-1]) 
    #print(tv_series[-2])
    #print(tv_series[-3])
    #test_filtra_por_edad(tv_series)
    test_valoracion_media_netflix(tv_series)

if __name__ == "__main__":
    main()
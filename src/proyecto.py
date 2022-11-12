import csv
from collections import namedtuple
from datetime import date, datetime
from unittest import result

tvshows=namedtuple('TvShows', 'ID, Title, Age, rating, Netflix, Hulu, Prime_Video, Disney_Plus, Release_Date')
def lee_datos(series):
    result = []
    with open (series, encoding= 'utf-8') as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)
        for lista in lector:
            ID = int(lista[0])
            Title= str(lista[1])
            Age = str(lista[2])
            rating=float(lista[3])
            Netflix=bool(lista[4])
            Hulu=bool(lista[5])
            Prime_Video=bool(lista[6])
            Disney_Plus=bool(lista[7])
            Release_Date=datetime.strptime(lista[8],"%d/%m/%Y")

            tupla_con_nombre = tvshows(ID, Title, Age, rating, Netflix, Hulu, Prime_Video, Disney_Plus, Release_Date)
            result.append(tupla_con_nombre)
    return result

def filtra_por_edad(tupla_con_nombre):
    result = []
    for i in tupla_con_nombre:
        if i.Age == 'all':
            result.append(i)
    return result


def valoracion_media_netflix(tupla_con_nombre):
    result = []
    for i in tupla_con_nombre:
        if i.Netflix == True:
            result.append(i.rating)
    return result

def valoraciones(tupla_con_nombre):
    result=[]
    for i in tupla_con_nombre:
        result.append(i.rating)
    return result

def max_valoracion_series_familiares(tupla_con_nombre):
    result=[]
    for i in filtra_por_edad(tupla_con_nombre):
        fin= (i.Title, i.Age, i.rating)
        if i.rating == max(valoraciones(tupla_con_nombre)):
            result.append(fin)
    return result

def agrupar_segun_fecha_lanzamiento(tupla_con_nombre):
    result = dict()
    for i in tupla_con_nombre:
        clave = i.Release_Date.year
        if clave in result:
            result[clave] += i
        else:
            result[clave] = i
    return result
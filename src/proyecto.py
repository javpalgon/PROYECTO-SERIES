import csv
from collections import namedtuple
from datetime import datetime
from parsers import *

tvshows=namedtuple('TvShows', 'id, Title, Age, rating, Netflix, Hulu, Prime_Video, Disney_Plus, Release_Date')
def lee_datos(series):
    result = []
    with open (series, encoding= 'utf-8') as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)
        for lista in lector:
            id = int(lista[0])
            Title= str(lista[1])
            Age = str(lista[2])
            rating=float(lista[3])
            Netflix=parsea_bool(lista[4])
            Hulu=parsea_bool(lista[5])
            Prime_Video=parsea_bool(lista[6])
            Disney_Plus=parsea_bool(lista[7])
            Release_Date=datetime.strptime(lista[8],"%d/%m/%Y")

            tupla_con_nombre = tvshows(id, Title, Age, rating, Netflix, Hulu, Prime_Video, Disney_Plus, Release_Date)
            result.append(tupla_con_nombre)
    return result

def series_para_todos(series):
    result = []
    for i in series:
        if i.Age == 'all':
            result.append(i)
    return result

def valoraciones(series):
    result=[]
    for i in series:
        result.append(i.rating)
    return result

def valoracion_media_netflix(series):
    result = []
    for i in series:
        if i.Netflix == True:
            result.append(i.rating)
    return (sum(result)/len(result))


def max_valoracion_series_familiares(series):
    result=[]
    for i in series_para_todos(series):
        fin = (i.Title, i.Age, i.rating)
        if i.rating == max(valoraciones(series)):
            result.append(fin)
    return result

def agrupar_segun_fecha_lanzamiento(series):
    result = dict()
    for i in series:
        clave = i.Release_Date.year
        if clave in result:
            result[clave] += i
        else:
            result[clave] = i
    return result

def total_series_por_anyo(series):
    series_por_anyo = dict()
    for s in series:
        if s.Release_Date.year in series_por_anyo:
            series_por_anyo[s.Release_Date.year] += 1
        else:
            series_por_anyo[s.Release_Date.year] =1
    return series_por_anyo.items()

def maximo_minimo_shows_por_anyo(series):
    tspa = total_series_por_anyo(series)
    maximo = max(tspa, key= lambda x: x[1])
    minimo = min(tspa, key= lambda x: x[1])
    return  maximo, minimo

def valoraciones_shows_por_edad(series, edad):
    result = []
    for s in series:
        titulo_valoracion = s.Title, s.rating
        if s.Age == edad:
            result.append(titulo_valoracion)
    return result

def mejor_serie_por_edad(series):
    dicc = dict()
    for s in series:
        if s.Age not in dicc:
            for s in series:
                dicc.setdefault(s.Age, max(valoraciones_shows_por_edad(series, s.Age), key= lambda x: x[1]))
    return dicc

def mejores_series_por_edad(series, n=3):
    diccionario = dict()
    for s in series:
        if s.Age not in diccionario:
            diccionario.setdefault(s.Age, sorted(valoraciones_shows_por_edad(series, s.Age), key= lambda x:x[1], reverse = True)[:n])
    return diccionario

def top_series_ninyos_Disney_Plus(series, n=5):
    result = []
    for s in series:
        if s.Disney_Plus == True and s.Age == '7+':
            result.append((s.Title, s.rating))
    return sorted(result, key=lambda x: x[1], reverse=True)[:n]
            
            
        

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
            Release_Date= datetime.strptime(lista[8], "%d/%m/%Y").date()

            tupla_con_nombre = tvshows(ID, Title, Age, rating, Netflix, Hulu, Prime_Video, Disney_Plus, Release_Date)
            result.append(tupla_con_nombre)
    return result
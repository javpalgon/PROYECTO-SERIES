import csv
from collections import namedtuple
from unittest import result

tvshows=namedtuple('TvShows', 'ID, Title, Year, Age, IMDb, Rotten Tomatoes, Netflix, Hulu, Prime Video, Disney Plus,Type')
def lee_datos(series):
    result = []
    with open (series, encoding= 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
    for ID, Title, Year, Age, IMDb, Rotten_Tomatoes, Netflix, Hulu, Prime_Video, Disney_Plus, Type in lector:
        tupla_con_nombre = tvshows(int(ID), str(Title), int(Year), int(Age), float(IMDb), int(Rotten_Tomatoes), int(Netflix), int(Hulu), int(Prime_Video), int(Disney_Plus), int(Type))
        result.append(tupla_con_nombre)
    return result
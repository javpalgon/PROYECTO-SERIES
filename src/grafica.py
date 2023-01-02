from proyecto import * 
from matplotlib import pyplot as plt
from collections import Counter

def total_series_segun_edad(series):
    series_segun_edad = dict()
    for s in series:
        if s.Age in series_segun_edad:
            series_segun_edad[s.Age] += 1
        else:
            series_segun_edad[s.Age] =1
    return series_segun_edad

def grafica_numero_series_segun_edad(series):
    diccionario = total_series_segun_edad(series)
    plt.bar(range(len(diccionario)), diccionario.values(), align = 'center')
    plt.xticks(range(len(diccionario)), diccionario.keys())
    plt.title("Comparativa de shows por edad:")
    plt.show()
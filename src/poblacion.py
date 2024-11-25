import csv
from collections import namedtuple
import matplotlib.pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblacion(fichero):
    res = []
    with open(fichero, encoding='UTF-8') as f:
        lector = csv.reader(f, delimiter=',')
        for pais, codigo, año, censo in lector:
            pais = str(pais)
            codigo = str(codigo)
            año = int(año)
            censo = int(censo)
            res.append(RegistroPoblacion(pais, codigo, año, censo))
    return res

def calcula_paises(poblacion):
    res = []
    for pob in poblacion:
        if pob.pais not in res:
            res.append(pob.pais)
    return sorted(res)

def filtra_por_pais(poblacion, cont):
    res = []
    for pob in poblacion:
        if pob.pais == cont or pob.codigo == cont:
            res.append(pob.año); res.append(pob.censo)
    return res

def filtra_por_pais_y_anyo(poblacion, cont, anyo):
    res = []
    for pob in poblacion:
        if pob.pais in cont and pob.año == anyo:
            res.append(pob.pais); res.append(pob.censo)
    return res

def muestra_evolucion_poblacion(poblacion, cont):
    lista_años = []
    lista_habitantes = []
    for pob in poblacion:
        if pob.pais == cont or pob.codigo == cont:
            lista_años.append(pob.año); lista_habitantes.append(pob.censo)
    plt.title("Gráfica")
    plt.plot(lista_años, lista_habitantes)
    plt.show()

def muestra_comparativa_paises_anyo(poblacion, anyo, cont):
    lista_paises = []
    lista_habitantes = []
    for pob in poblacion:
        if pob.pais in cont or pob.codigo in cont and pob.año == anyo:
            lista_paises.append(pob.pais); lista_habitantes.append(pob.censo)
    plt.title("Gráfica")
    plt.bar(lista_paises, lista_habitantes)
    plt.show()


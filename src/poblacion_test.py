from poblacion import *

def test_lee_poblacion(fichero):
    poblacion = lee_poblacion(fichero)
    print(poblacion)

def test_calcula_pais(poblacion):
    res = calcula_paises(poblacion)
    print(res)

def test_filtra_por_pais(poblacion, cont):
    res = filtra_por_pais(poblacion, cont)
    print(res)

def test_filtra_por_pais_y_anyo(poblacion, cont, anyo):
    res = filtra_por_pais_y_anyo(poblacion, cont, anyo)
    print(res)

def test_muestra_evolucion_poblacion(poblacion, cont):
    muestra_evolucion_poblacion(poblacion, cont)

def test_muestra_comparativa_paises_anyo(poblacion, anyo, cont):
    muestra_comparativa_paises_anyo(poblacion, anyo, cont)
    


if __name__ == '__main__':
    fichero = 'data\population.csv'
    poblacion = lee_poblacion(fichero)
    paises = {'United States', 'ESP'}
    #test_lee_poblacion(fichero)
    #test_calcula_pais(poblacion)
    #test_filtra_por_pais(poblacion, 'USA')
    #test_filtra_por_pais_y_anyo(poblacion, paises, 2000)
    #test_muestra_evolucion_poblacion(poblacion, 'USA')
    test_muestra_comparativa_paises_anyo(poblacion, 2000, paises)

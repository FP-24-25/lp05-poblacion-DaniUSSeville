import csv
from collections import namedtuple
import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt



def lee_poblaciones(ruta_fichero:csv):
    """
    _summary_

    :param ruta_fichero: ruta que dirige al fichero cs
    :type ruta_fichero: csv
    :return: todos los datos del csv
    :rtype: lista de tuplas
    """    
    RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')
    registros = []
    with open(ruta_fichero, mode="r", encoding='utf-8') as f:
        lector = csv.reader(f, delimiter =",")
        
        for linea in lector:
            registros.append(RegistroPoblacion(str(linea[0]), #Pais
                                                str(linea[1]), #Codigo
                                                datetime.datetime.strptime(linea[2], "%Y").year, #Año
                                                int(linea[3]), #Censo 
                                                ))

    return registros 


def calcula_paises(poblaciones):
    res = [e for e in poblaciones]
        
    res_ordenado = sorted(res, key=lambda x: (x.pais)) 

    for e in res_ordenado:
        print(f"Pais: {e.pais}")
        


def filtrar_por_pais(poblaciones,nombre_o_codigo):
    res = [e for e in poblaciones if nombre_o_codigo.upper() == e.pais.upper() or nombre_o_codigo.upper() == e.codigo.upper()]
        
    for e in res:
        print(f"Pais: {e.pais} , Codigo: {e.codigo}, Año: {e.año}, Censo: {e.censo}")
        



def filtrar_por_pais_y_anyo(poblaciones:tuple,anyo:datetime,paises:list):
    anyo = datetime.datetime.strptime(anyo, "%Y")
    anyo = anyo - relativedelta(years=1)

    res = {e for e in poblaciones if anyo.year == e.año and e.pais in paises}
        
    for e in res:
        print(f"Pais: {e.pais} , Habitantes: {e.censo}")
        
        
        
def muestra_evolucion_poblacion(poblaciones,nombre_o_codigo):
    res = [e for e in poblaciones if nombre_o_codigo.upper() == e.pais.upper() or nombre_o_codigo.upper() == e.codigo.upper()]
    lista_años = [int(e.año) for e in res]
    lista_habitantes = [e.censo for e in res]
    
    plt.title(f"Crecimientos habitantes por año en {nombre_o_codigo}")
    plt.plot(lista_años, lista_habitantes)
    plt.show()   
   
   
    
def muestra_comparativa_paises_anyo(poblaciones:list,anyo:datetime,paises:str):
    anyo = datetime.datetime.strptime(anyo, "%Y")
    paisesEntrantes = [e for e in poblaciones if e.año == anyo.year and e.pais in paises]

    lista_paises = [e.pais for e in paisesEntrantes]
    lista_habitantes = [e.censo for e in paisesEntrantes]
    
    plt.title("Cantidad de habitantes")
    plt.bar(lista_paises, lista_habitantes)
    plt.show()
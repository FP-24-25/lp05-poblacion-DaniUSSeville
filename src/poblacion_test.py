from poblacion import *

if __name__ == "__main__":
    registros = lee_poblaciones("data/population.csv")
    #calcula_paises(registros)
    #filtrar_por_pais(registros,"caribbean small states")
    
    paises= ["Arab World","Caribbean small states"]
    
    #filtrar_por_pais_y_anyo(registros,"1975",paises)
    #muestra_evolucion_poblacion(registros,"css")
    
    muestra_comparativa_paises_anyo(registros,"1975",paises)
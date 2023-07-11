import numpy as np
import time
import statistics
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count

def funcion_sincrona(vectorA,vectorB,N):
    norma = 0
    for i in range(N):
        norma += (vectorB[i]-vectorA[i])**2
    return norma**(1/2)

def funcion_multihilo(vectorA,vectorB,executor):
    return sum(list(executor.map(auxiliar,[[vectorA,vectorB,inicio,cant_hilos] for inicio in range(cant_hilos)])))**(1/2)

def funcion_multiproceso(vectorA,vectorB,pool):
    return sum(list(pool.map(auxiliar,[[vectorA,vectorB,inicio,cant_procesos] for inicio in range(cant_procesos)])))**(1/2)

def auxiliar(datos):
    return sum([pow((datos[1][i]-datos[0][i]),2) for i in range(datos[2],len(datos[1]),datos[3])])

if __name__ == '__main__':
    N = 4096
    vectorA = np.random.rand(N)
    vectorB = np.random.rand(N)
    
    lista_tiempos1 = list()
    for i in range(100):
        inicio1 = time.perf_counter()
        funcion_sincrona(vectorA,vectorB,N)
        lista_tiempos1.append(time.perf_counter()-inicio1)
    mediana1 = statistics.median(lista_tiempos1)
    print(f"El tiempo de ejecución de la función sincrona es: {mediana1}")
    
    lista_tiempos2 = list()
    cant_hilos = 8
    Threads = ThreadPoolExecutor(max_workers=cant_hilos)
    for i in range(100):
        inicio2 = time.perf_counter()
        funcion_multihilo(vectorA,vectorB,Threads)
        lista_tiempos2.append(time.perf_counter()-inicio2)
    mediana2 = statistics.median(lista_tiempos2)
    print(f"El tiempo de ejecución de la función multihilo es: {mediana2}")
    
    lista_tiempos3 = list()
    cant_procesos = cpu_count()
    Procesos = Pool(processes=cant_procesos)
    for i in range(100):
        inicio3 = time.perf_counter()
        funcion_multiproceso(vectorA,vectorB,Procesos)
        lista_tiempos3.append(time.perf_counter()-inicio3)
    Procesos.close()
    Procesos.join()
    mediana3 = statistics.median(lista_tiempos3)
    print(f"El tiempo de ejecución de la función multiproceso es: {mediana3}")
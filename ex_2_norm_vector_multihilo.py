"""
Enunciado específico:
Implementar el programa norm_vectorial_multihilo.py el cual permite calcular la norma vectorial en su versión utilizando multihilos. 
Hallar el tiempo de ejecución considerando el tiempo representativo con medidas de tendencia central.
Evidenciar su resultado utilizando capturas de pantalla.
"""
"""
Función que calcula la norma vectorial de 2 vectores con valores aleatorios utilizando multihilos.
Dividiremos el vector en 8 partes iguales, donde 8 es el número de hilos que se utilizarán (escogemos
este número para que sea igual a la cantidad de procesos que utilizaremos en la implementación paralela usando multiprocessing).
Luego, cada hilo calculará la norma de su parte del vector (suma de cuadrados de las distancias de cada componente).
Finalmente, se sumarán las normas de cada hilo para obtener la norma total (se extraerá la raíz cuadrada al final).
La función recibirá como parámetro de entrada un ID de hilo, a parte de los vectores A y B, que servirá para diferenciar
las partes del vector que le corresponde a cada hilo y realizar los cálculos específicos en cada caso.
Inputs:
    A: vector de tamaño 4096 con valores aleatorios
    B: vector de tamaño 4096 con valores aleatorios
    ID: ID del hilo (tomarán valores del 1 al 8)
"""
import statistics
import random
import threading
import time
import math
TOTAL=[]
def norm_vector_multihilo(ID, A,B):
    global TOTAL
    sum = 0
    A_aux = A[(ID-1)*512 : ID*512]
    B_aux = B[(ID-1)*512 : ID*512]

    for j in range(len(A_aux)):
        ele = (A_aux[j]-B_aux[j])**2
        sum = sum +ele
    TOTAL.append(sum)
    return sum

if __name__ == "__main__":
    tiempos = [ ]
    for _ in range(100):
        TOTAL=[]
        A= [ ]
        for j in range(4096):
            A.append(random.randint(1,100))
        B= [ ]
        for j in range(4096):
            B.append(random.randint(1,100))
        #tic = time.perf_counter()
        argus = [ ]
        for u in range(8):
            argus.append((u+1,A,B ))
        tic = time.perf_counter()
        Thread_0 = threading.Thread(target= norm_vector_multihilo ,args = (argus[0])) 
        Thread_1 = threading.Thread(target= norm_vector_multihilo ,args = (argus[1])) 
        Thread_2 = threading.Thread(target= norm_vector_multihilo ,args = (argus[2])) 
        Thread_3 = threading.Thread(target= norm_vector_multihilo ,args = (argus[3])) 
        Thread_4 = threading.Thread(target= norm_vector_multihilo ,args = (argus[4])) 
        Thread_5 = threading.Thread(target= norm_vector_multihilo ,args = (argus[5])) 
        Thread_6 = threading.Thread(target= norm_vector_multihilo ,args = (argus[6])) 
        Thread_7 = threading.Thread(target= norm_vector_multihilo ,args = (argus[7])) 
        Thread_0.start()
        Thread_1.start()
        Thread_2.start()
        Thread_3.start()
        Thread_4.start()
        Thread_5.start()
        Thread_6.start()
        Thread_7.start()
        Thread_0.join()
        Thread_1.join()
        Thread_2.join()
        Thread_3.join()
        Thread_4.join()
        Thread_5.join()
        Thread_6.join()
        Thread_7.join()
        aux = 0
        for i in TOTAL:
            aux= aux+i
        rpta = math.sqrt(aux)
        print(rpta)
        toc = time.perf_counter()
        tiempos.append(toc-tic)
    print(f"El tiempo de ejecucion de la funcion multihilos es { statistics.median(tiempos)*10**6} MICROsegundos")        


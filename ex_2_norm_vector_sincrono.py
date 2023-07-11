"""
Enunciado general:

Se requiere la mejor forma de implementar la norma vectorial de 2 vectores con valores aleatorios.
Los vectores son de tamaño de 4096. Para ello, recordar que la definición es la siguiente:

norma(AB) = sqrt((B1 - A1)^2 + (B2 - A2)^2 + ... + (Bn - An)^2)
"""

"""
Enunciado específico:
Implementar el programa norm_vectorial_sincrono.py el cual permite calcular la norma vectorial en su versión síncrona.
Hallar el tiempo de ejecución considerando el tiempo representativo con medidas de tendencia central.
Evidenciar su resultado utilizando capturas de pantalla.
"""
"""
Función que calcula la norma vectorial de 2 vectores con valores aleatorios.
Inputs:
    A: vector de tamaño 4096 con valores aleatorios
    B: vector de tamaño 4096 con valores aleatorios
Output:
    La norma vectorial de A y B
"""
import random
import statistics
import math
import time
def norm_vector_sincrono(A,B):
    sum = 0
    for j in range(len(A)):
        ele = (A[j]-B[j])**2
        sum=sum+ele
    sum = math.sqrt(sum)
    #print(sum)
    return sum
"""
Enunciado general:

Se requiere la mejor forma de implementar la norma vectorial de 2 vectores con valores aleatorios.
Los vectores son de tamaño de 4096. Para ello, recordar que la definición es la siguiente:

norma(AB) = sqrt((B1 - A1)^2 + (B2 - A2)^2 + ... + (Bn - An)^2)
"""

if __name__ == "__main__":
    #SINCRONA
    tiempos = []
    for h in range(1000):
        #tic = time.perf_counter()        
        A= [ ]
        for j in range(4096):
            A.append(random.randint(1,100))
        B= [ ]
        for j in range(4096):
            B.append(random.randint(1,100))
        tic = time.perf_counter()
        norm_vector_sincrono(A,B)
        toc = time.perf_counter()
        tiempos.append(toc-tic)
    mediana = statistics.median(tiempos)
    print(f"La mediana es  { mediana} segundos")
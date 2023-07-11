import time
from multiprocessing import Pool ,Manager
"""
Enunciado general:

Se requiere la mejor forma de implementar la norma vectorial de 2 vectores con valores aleatorios.
Los vectores son de tamaño de 4096. Para ello, recordar que la definición es la siguiente:

norma(AB) = sqrt((B1 - A1)^2 + (B2 - A2)^2 + ... + (Bn - An)^2)
"""

"""
Enunciado específico:
Implementar el programa norm_vectorial_multiprocessing.py el cual permite calcular la norma vectorial en su 
versión utilizando multiprocessing. Hallar el tiempo de ejecución considerando el tiempo representativo con 
medidas de tendencia central. Evidenciar su resultado utilizando capturas de pantalla.
"""
import random
import statistics
def norm_vector_multipro(ID, A,B,result_list):
    sum = 0
    #A_aux = A[(ID-1)*512 : ID*512]
    #B_aux = B[(ID-1)*512 : ID*512]
    for j in range((ID-1)*512 , ID*512):
        ele = (A[j]-B[j])**2
        sum = sum +ele
    result_list.append(sum)
    
if __name__ == "__main__":
    tiempos = []
    counter=1
    for h in range(100):
        #tic = time.perf_counter()
        manager=Manager()
        result_list= manager.list()
        A= [ ]
        for j in range(4096):
            A.append(random.randint(1,100))
        B= [ ]
        for j in range(4096):
            B.append(random.randint(1,100))
        p=Pool(processes=8)
        args= [(ID,A,B,result_list) for ID in range(1,9)]
        tic =time.perf_counter()
        p.starmap(norm_vector_multipro,args)
        p.close()
        p.join()
        #pr    int(aux)
        suma=sum(result_list)
        rpta =(suma)**(1/2)
        print(rpta)
        toc =time.perf_counter() 
        tiempos.append(toc-tic)
        print(counter)
        counter=counter+1
    mediana = statistics.median(tiempos)
    print(f"La mediana es  { mediana} segundos")
import random , statistics ,threading,time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count
import numpy as np
A = []
B = []
for i in range(4096):
    A.append(random.randint(1,100))
    B.append(random.randint(1,100))
def elegir_intervalo(ID,i):
    step = int(4096/i)
    if i==8:
        inicio=step*(ID-1)
        fin = step*(ID)
    elif i==7:
        if ID != 7:
            inicio= step* (ID-1)
            fin =step*(ID)
        else:
            inicio= 3510
            fin = 4096
    elif i==6:
        if ID != 6:
            inicio= step*(ID-1)
            fin = step*(ID)
        else:
            inicio= 3410
            fin = 4096
    elif i==5:
        if ID != 5:
            inicio= step*(ID-1)
            fin = step*(ID)
        else:
            inicio= 3410
            fin = 4096
    elif i==4:
        if ID != 4:
            inicio= step*(ID-1)
            fin = step*(ID)-1
        else:
            inicio= 3410
            fin = 4096-1
    elif i==3:
        if ID != 3:
            inicio= step*(ID-1)
            fin = step*(ID)
        else:
            inicio= 2730
            fin = 4096-1    
    elif i==2:
        if ID != 2:
            inicio= step*(ID-1)
            fin = step*(ID)
        else:
            inicio= 2048
            fin = 4096-1
    elif i==1:
        inicio=0
        fin = 4096-1
def norm_sincrono ( A,B):
    suma = 0
    for _ in range(len(A)):
        suma = suma + (A[_]- B[_])**2
    rpta =suma**(1/2)
    return rpta

def aux_norm(entrada):
    ID,A,B,i=entrada
    sum=0
    step = int(len(A)/i)
    inicio = step*(ID-1)
    print(inicio)
    fin = step*(ID)
    print(fin)
    for i in range(inicio,fin):
        sum = sum + (A[i] -B[i])**2
    #for i,j in zip(A[(ID-1)*int(len(A)/i) : ID*int(len(A)/i)],B[(ID-1)*int(len(A)/i) : ID*int(len(A)/i)]):
    #    sum = sum + (i-j)**2
    #print(sum)
    return sum
def aux_norm_2(ID,A,B,i):
    sum=0
    step = int(len(A)/i)
    inicio = step*(ID-1)
    fin = step*(ID)
    for j in range(inicio,fin):
        sum = sum + (A[j] -B[j])**2
    #for i,j in zip(A[(ID-1)*int(len(A)/i) : ID*int(len(A)/i)],B[(ID-1)*int(len(A)/i) : ID*int(len(A)/i)]):
    #    sum = sum + (i-j)**2
    #print(sum)
    return sum
if __name__ == "__main__":
    hilos = [cpu_count()]
    for i in hilos:
        #PARTE_SERIAL
        tiempos_serial = []
        for h in range(1000):
            tic = time.perf_counter()
            rpta_serial =norm_sincrono(A,B)
            toc =time.perf_counter()
            tiempos_serial.append(toc-tic)
        print(f"El tiempo promedio de ejecucion de la funcion serial es de { statistics.median(tiempos_serial)* (10**6)}microsegundos")
        #PARTE_MULTIHILO
        tiempos_multihilo =[]
        PoolThreads =ThreadPoolExecutor(max_workers=i)
        for h in range(1000):
            tic=time.perf_counter()
            respuestas= list(PoolThreads.map(aux_norm,([ID,A,B,i]for ID in range(1,i))))
            rpta_hilo = sum(respuestas) **(1/2)             
            toc=time.perf_counter()
            tiempos_multihilo.append(toc-tic)        
        print(f"El tiempo promediode la funcion multihilo es de { statistics.median(tiempos_multihilo)*(10**6)} microsegundos con {i} hilos")
        #PARTE_MULTIPROCCESSING
        tiempos_multi = []
        p=Pool(processes=i)
        for h in range(1000):
            tic = time.perf_counter()
            resultados = p.starmap(aux_norm_2,([ID,A,B,i]for ID in range(1,i)))
            rpta_multipro= sum(resultados) ** (1/2)
            toc = time.perf_counter()
            tiempos_multi.append(toc-tic)
        time.sleep(20)
        print(f"El tiempo promediode la funcion multiprocessing es de { statistics.median(tiempos_multi) * (10**6)} microsegundos con {i} procesos")
        print(rpta_hilo)
        print(rpta_multipro)
        print(rpta_serial)

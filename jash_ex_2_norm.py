import math,time,numpy as np
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool


array1=np.random.randint(0,1000,size=4096)
array2=np.random.randint(0,1000,size=4096)
cantHilos=[1,2,3,4,5,6,7,8]
cantProcesos=[1,2,3,4,5,6,7,8]

def sincrono(array1,array2):
    norma=0
    for i in range(len(array1)):
        norma+=(array1[i]-array2[i])**2
    return norma**(1/2)

def auxParalelo(input):
    array1,array2,inicio,workers=input
    norma=0
    for i in range(inicio,len(array1),workers):
        norma+=(array1[i]-array2[i])**2
    return norma

def multiThreading(array1,array2):
    #print( pow(sum(list(PoolThreads.map(auxParalelo,([array1,array2,i,hilos] for i in range(hilos))))),1/2))
    return pow(sum(list(PoolThreads.map(auxParalelo,([array1,array2,i,hilos] for i in range(hilos))))),1/2)

def multiProcessing(array1,array2):
    return pow(sum(PoolProcesses.map(auxParalelo,([array1,array2,i,procesos] for i in range(procesos)))),1/2)

if __name__ == '__main__':
    for hilos,procesos in zip(cantHilos,cantProcesos):
        listaTiemposSerial=[]
        listaTiemposMultiThreading=[]
        listaTiemposMultiProcessing=[]
        for i in range(1000):
            t=time.perf_counter()
            resultadoSincrono=sincrono(array1,array2)
            listaTiemposSerial.append(time.perf_counter()-t)
        print(f"Se empleó un total de {np.median(listaTiemposSerial)*1e6} microsegundos aproximadamente para realizar la norma vectorial de 2 arreglos de forma serial.")
        PoolThreads=ThreadPoolExecutor(max_workers=hilos)
        for i in range(100):
            t=time.perf_counter()
            resultadoMultiThreading=multiThreading(array1,array2)
            listaTiemposMultiThreading.append(time.perf_counter()-t)
        print(f"Se empleó un total de {np.median(listaTiemposMultiThreading)*1e6} microsegundos aproximadamente para realizar la norma vectorial de 2 arreglos de forma paralela usando MultiThreading con {hilos} hilos.")
        PoolProcesses=Pool(processes=procesos)
        for i in range(100):
            t=time.perf_counter()
            resultadoMultiProcessing=multiProcessing(array1,array2)
            listaTiemposMultiProcessing.append(time.perf_counter()-t)
        print(f"Se empleó un total de {np.median(listaTiemposMultiProcessing)*1e6} microsegundos aproximadamente para realizar la norma vectorial de 2 arreglos de forma paralela usando MultiProcessing con {procesos} procesos.")
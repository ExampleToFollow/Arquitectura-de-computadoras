import random, statistics, time ,threading
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
def crear_arreglo():
    A=[]
    for j in range(4096):
        A.append(random.randint(1,1000))
    return A

def norm_vector_sincrono(A,B):
    suma=0
    for i in range(len(A)):
        ele = (A[i]-B[i])**2
        suma=suma+ ele
#    for i,j in zip(A,B):
#        suma=suma+ (i-j)**2
    rpta =suma**(1/2)
    return rpta

TOTAL =[]
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

def norm_vector_multihilo_1(entrada):
    ID,A,B,i = entrada
    sum = 0
    step= int(len(A)/i)
    A_aux = A[(ID-1)*step : ID*step]
    B_aux = B[(ID-1)*step : ID*step]

    for j in range(len(A_aux)):
        ele = (A_aux[j]-B_aux[j])**2
        sum = sum +ele
    return sum

def norm_thread_2(A,B,i):
    PoolThreads = ThreadPoolExecutor(max_workers=i)
    #aux= ([ID,A,B] for ID in range(1,i+1))
    ola = list(PoolThreads.map(norm_vector_multihilo_1,([ID,A,B,i]for ID in range(1,i+1))))
    suma = sum(ola)
    suma = suma**(1/2)
    #print(suma)
    return suma

def norm_vector_multipro(ID, A,B,i):
    sum = 0
    #step = int(len(A)/i)
    #A_aux = A[(ID-1)*step : ID*step]
    #B_aux = B[(ID-1)*step : ID*step]
    for i,j in zip(A[(ID-1)*int(len(A)/i) : ID*int(len(A)/i)],B[(ID-1)*int(len(A)/i) : ID*int(len(A)/i)]):
        sum = sum + (i-j)**2
    return sum

if __name__ == "__main__":
    thread_process = [1,2,3,4,5,6,7,8]
    A= crear_arreglo()
    B= crear_arreglo()
    #thread_process = [6,7,8]
    for i in thread_process:
        tiempos_sincrono = []
        tiempos_thread = []
        tiempos_thread_2 = []
        tiempos_multi = []
        counter=0
        for h in range(1000):
            TOTAL=[]
            #tic = time.perf_counter()        
            #FUNCION SINCRONA
            tic = time.perf_counter()
            rpta_sincrono = norm_vector_sincrono(A,B)
            toc = time.perf_counter()
        tiempos_sincrono.append(toc-tic)
        for h in range(1000):
            #PRIMERA FORMA DE HACERLO CON THREADS
            tic = time.perf_counter()
            argus = [(ID,A,B) for ID in range(1,9)]
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
            rpta_thread_1 =sum(TOTAL)**(1/2)        
            toc = time.perf_counter()
            tiempos_thread.append(toc-tic)
        
        for h in range(1000):
            #SEGUNDA FORMA DE HACERLO CON THREADS
            tic = time.perf_counter()
            rpta_thread_2 =norm_thread_2(A,B,i)
            toc = time.perf_counter()
            tiempos_thread_2.append(toc-tic)
            #print(rpta_thread_1)
            #print(rpta_sincrono)
            #print(rpta_thread_2)
        p=Pool(processes=i)
        args= [(ID,A,B,i) for ID in range(1,9)]
        for h in range(1000):
            #TERCERA FORMA DE HACERLO CON PROCESSING
            #p=Pool(processes=i)
            #args= [(ID,A,B,i) for ID in range(1,9)]
            tic = time.perf_counter()
            resultados = sum(p.starmap(norm_vector_multipro,args))**(1/2)
            #resultados = sum(resultados) ** ( 1/2)
            #print(resultados)
            toc= time.perf_counter()
            tiempos_multi.append(toc-tic)
        counter= counter+1
            #print(counter)
        mediana_sincrono = statistics.median(tiempos_sincrono)
        mediana_thread = statistics.median(tiempos_thread)
        mediana_thread_2 =statistics.median(tiempos_thread_2)
        mediana_multi = statistics.median(tiempos_multi)
        print(f"La mediana de la funcion sincrona es  {mediana_sincrono*(10**6)} microsegundos")
        print(f"La mediana de la funcion multihilo es  {mediana_thread*(10**6)} microsegundos")
        print(f"La mediana de la funcion multihilo_2 es  {mediana_thread_2*(10**6)} microsegundos con { i } hilos")
        print(f"La mediana de la funcion multipro es  {mediana_multi*(10**6)} microsegundos con {i } procesos")

import time
from multiprocessing import Pool, Manager
def f_serial(x):
    suma=0
    #sys.set_int_max_str_digits(suma)
    for i in range (1,10001):
        suma += i*(x**i)
    return suma

def f_paralelo(x,rango):
    suma  = 0 
    for j in range(rango-2500+1 ,rango+1):
        suma =suma + j*(x**j)
    return suma  

if __name__ == "__main__":
    print("Parte serial")
    tic = time.perf_counter()
    suma_serial = f_serial(2023)
    toc = time.perf_counter()
    time_serial = toc-tic
    print(f"tiempo de ejecucion de la funcion serial es de {time_serial}")
    print("Parte paralela:")    
    tic=time.perf_counter()
    p=Pool(processes=4)
    iter= [2500,5000,7500,10000]
    args= [(2023,i)for i in iter]
    #tic= time.perf_counter()
    aux=p.starmap(f_paralelo,args)
    p.close()
    p.join()
    suma_paralelo=sum(aux)
    toc = time.perf_counter()
    time_paralelo= toc-tic
    print(f"La parte en paralelo es de {time_paralelo} segundos")
    print(f"El speeUp es de {time_serial/time_paralelo }")
    assert suma_paralelo==suma_serial
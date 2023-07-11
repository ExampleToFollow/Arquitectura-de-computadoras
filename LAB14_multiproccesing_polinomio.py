import time
from multiprocessing import Pool
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
    tic = time.perf_counter()
    resultado_serial = f_serial(2023)
    toc = time.perf_counter()
    time_serial = toc-tic
    print(f"El tiempo de ejecucion de la funcion serial es de {time_serial} segundos")    
    tic=time.perf_counter()
    p=Pool(processes=4)
    iter= [2500,5000,7500,10000]
    args= [(2023,i)for i in iter]
    #tic= time.perf_counter()
    aux=p.starmap(f_paralelo,args)
    p.close()
    p.join()
    resultado_paralelo=sum(aux)
    toc = time.perf_counter()
    time_paralelo= toc-tic
    print(f"EL tiempo de ejecución de la funcion en paralelo es de {time_paralelo} segundos")
    print(f"El speeUp es de {time_serial/time_paralelo }")
    assert resultado_paralelo==resultado_serial
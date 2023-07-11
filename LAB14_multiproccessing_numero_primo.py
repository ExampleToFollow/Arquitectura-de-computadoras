import time
from multiprocessing import Pool , Manager
def es_primo_serial(n):
    x = True
    for i in range(2,int(n**(1/2))+1):
        if n%i == 0:
            x= False
            return x
    return x    

def es_primo_paralelo(n,aux,inicio,fin):
    x=True
    for i in range(inicio,fin+1):
        if n%i==0 and not aux.value :
            print(i)
            x=False
            aux.value = True
            return x
    return x

def partir_inter(n):
    aux_1 = int(n**0.5)
    if aux_1 %2 ==0:
        step_2 = aux_1/2
        step_3 = aux_1
    else:
        step_2 = int((aux_1)/2)
        step_3 = aux_1
    return [step_2 ,step_3]
#Basta con que un valor de la lista sea falso (porque se debio reconocer al menos un numero divisible) se debe retorna el valor 
def elegir(lista):
    for i in lista:
        if i==False:
            return i
    return True

def bucle_primo(x):
    #manager = Manager()
    #auxiliar = manager.Value('b',False)
    auxiliar =False
    p = Pool(processes=2)
    args = [(x,'primero',auxiliar), (x,'segundo',auxiliar)]
    lista = p.starmap(es_primo_bucle,args)
    #print(lista)
    if lista[0]<lista[1]:
        return lista[0]
    else:
        return lista[1]

def es_primo_bucle(x,step,auxiliar):
    if es_primo_serial(x+1):
        return x+1
    elif es_primo_serial(x+2):
        return x+2
    if  not es_primo_serial(x+1):
        if x%2 ==0 and step=='primero':
            if es_primo_serial(x+1):
                x_t=x+1
                while(True and not auxiliar):
                    x_t = x_t+4
                    if (es_primo_serial(x_t)):
                        auxiliar=True
                        return x_t
            else:
                x_t=x+1
                while(True and not auxiliar):
                    x_t = x_t+4
                    if (es_primo_serial(x_t)):
                        auxiliar=True
                        return x_t
                
        elif x%2 !=0 and step == 'primero':
            if es_primo_serial(x+2):
                x_t=x+2
                while(True and not auxiliar):
                    x_t = x_t+4
                    if (es_primo_serial(x_t)):
                        auxiliar=True
                        return x_t
            else:
                x_t=x+2
                while(True and not auxiliar):
                    x_t = x_t+4
                    if (es_primo_serial(x_t)):
                        auxiliar=True
                        return x_t
        elif x%2==0 and step=='segundo':
            if es_primo_serial(x+3):
                x_t=x+3
                while(True and not auxiliar):
                    x_t = x_t+4
                    if (es_primo_serial(x_t)):
                        auxiliar=True
                        return x_t
            else:
                x_t=x+3
                while(True and not auxiliar):
                    x_t = x_t+4
                    if (es_primo_serial(x_t)):
                        auxiliar=True
                        return x_t
        elif x%2 !=0 and step == 'segundo':
            if es_primo_serial(x+4):
                x_t=x+4
                while(True and not auxiliar):
                    x_t = x_t+4
                    if (es_primo_serial(x_t)):
                        auxiliar=True
                        return x_t
            else:
                x_t=x+4
                while(True and not auxiliar):
                    x_t = x_t+4
                    if (es_primo_serial(x_t)):
                        auxiliar=True
                        return x_t
                
if __name__ == "__main__":
    num= 2_345_678_911_111_111
    #num = 202300000
    #num= 7000
    #PARTE_A
    tic =time.perf_counter()
    respuesta_serial=es_primo_serial(num)
    toc = time.perf_counter()
    time_serial = toc-tic
    print(f"el tiempo de ejecucion de la funcion serial es {time_serial} segundos")
    print(f"L a respuesta de la funcion serial fue {respuesta_serial}")
    #PARTE_B
    tic =  time.perf_counter()
    manager = Manager()
    aux = manager.Value('b', False)
    p = Pool(processes = 2)
    intervalos = partir_inter(num)
    args = [(num,aux,2, intervalos[0]),(num,aux,intervalos[0], intervalos[1])]
    lista=p.starmap(es_primo_paralelo,args)
    p.close()
    p.join()
    respuesta_paralelo=elegir(lista)
    toc = time.perf_counter()
    time_paralelo = toc-tic
    print(f"el tiempo de ejecucion de la funcion paralelo es {time_paralelo} segundos")
    print(f"La respuesta de la funcion paralela fue {respuesta_paralelo}")
    print(f"EL speedUp es de {time_serial/time_paralelo}")
    #PARTE_C
    #puede alterar el valor de x
    x=24
    tic = time.perf_counter()
    resultado_bucle=bucle_primo(x)
    print(f"EL siguiente numero primo encontrado es {resultado_bucle}")
    toc = time.perf_counter()
    time_bucle=toc-tic
    print(f"el tiempo de ejecucion de la funcion bucle es {time_bucle} segundos")
    print(f"El proximo primo es {resultado_bucle}")
    assert respuesta_paralelo == respuesta_paralelo

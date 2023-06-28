import time
def es_primo(n):
    x = True
    for i in range(2,int(n**(1/2))+1):
        if int(n/i) == n/i :
            x= False
            return x
    return x    


if __name__ == "__main__":
    tic =time.perf_counter()
    es_primo( 2_345_678_911_111_111)
    toc = time.perf_counter()
    time_serial = toc-tic
    print(f"el tiempo de ejecucion de la funcion paralela se demora {time_serial}")
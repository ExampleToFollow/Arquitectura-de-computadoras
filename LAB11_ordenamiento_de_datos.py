#import sys
import time
def abrir_csv():
    with open("pacientes.csv", "r") as f:
        contenido = f.read()
    filas = contenido.split("\n")
    return filas[1:] 

if __name__ == "__main__":

    #filas =abrir_csv()
    N = int(input(">"))
    edad_N = []
    #porque 
    j=1
    # empieza tiempo de lectura
    tic=time.perf_counter()
    filas =abrir_csv()
    for i in filas[:N]:
        sub_filas = i.split(",")
        edad_N.append([sub_filas[4],i])
    toc= time.perf_counter()
    #termina tiempo de lectura
    time_read = toc-tic
    #print(edad_N)    
    #ordenado
    tic = time.perf_counter()
    ordenado = sorted(edad_N, key=lambda edad: edad[0])
    toc = time.perf_counter()
    time_order = toc-tic
    #print(ordenado)
    #tiempo de escritura
    tic = time.perf_counter()
    for j in range(len(ordenado)):
        with open("pacientes_ordenado.csv","a") as f:
                f.write(ordenado[j][1])
                f.write("\n")
    toc = time.perf_counter()
    time_write = toc-tic
    tup = (time_read , time_write , time_order)
    print(f"el tiempo de lectura fue de {tup[0]} , el tiempo de escritura fue de {tup[1]} y el tiempo de ordenamiento fue de {tup[2]}")


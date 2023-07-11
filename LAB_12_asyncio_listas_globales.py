import random
import asyncio
import time
subastadores= ['Telefonica','Claro','Entel']
#variables GLOBALES
precio_0 = [15,15,15]
#letra_0= ['','','']
max_0 = max(precio_0)
precio_1 = [15,15,15]
#letra_1= ['','','']
max_1=max(precio_1)
precio_2 = [15,15,15]
#letra_2= ['','','']
ran = [0,1,2,10,12,20,120]
max_2=max(precio_2)
def max(lista):
    max= 0
    for i in lista:
        if i>max:
            max=i
    return max
#async with asyncio.timeout(60): da vida de 60 segundos
async def jugador(letra):
    global max_2 ,max_1,max_0
    i = random.randint(0,10)
    await asyncio.sleep(i)
    #Lo truncamos para que se pueda escoger bien el rango del numero aleatorio
    ofertado_0 = random.randint(max_0+2,int((1.2)*(max_0)))
    ofertado_1 = random.randint(max_1+2, int((1.2)*(max_1)))
    ofertado_2 = random.randint(max_2+2 , int(max_2*(1.2)))
    #la palabra josh es un auxiliar para la eleccion aleatoria de q elementos elegir 
    josh = random.choice(ran)
    #Creamos los casos para cada situacion q se pueda elegir
    if josh == 0:
        if ofertado_0>max_0:
            idx=subastadores.index(letra)
            precio_0[idx]=ofertado_0
            max_0=max(precio_0)
            print(f"El jugador {letra} ha reofertado { max_0} para el bloque 0")
    elif josh == 1:
        if ofertado_1>max_1:
            idx=subastadores.index(letra)
            precio_1[idx]=ofertado_1
            max_1=max(precio_1)
            print(f"El jugador {letra} ha reofertado { max_1} para el bloque 1")
    elif josh == 2:
        if ofertado_2>max_2:
            idx=subastadores.index(letra)
            precio_2[idx]=ofertado_2
            max_2=max(precio_2)
            print(f"El jugador {letra} ha reofertado { max_2} para el bloque 2")
    elif josh == 10:
        if ofertado_1>max_1 and ofertado_0>max_0:
            maximo = max([ofertado_1,ofertado_0])
            idx=subastadores.index(letra)
            precio_1[idx]=maximo
            max_1=max(precio_1)
            precio_0[idx]=maximo
            max_0=max(precio_0)
            print(f"El jugador {letra} ha reofertado { maximo}  para el bloque 0 y 1")
    elif josh == 12:
        if ofertado_1>max_1 and ofertado_2>max_2:
            maximo = max([ofertado_1,ofertado_2])
            idx=subastadores.index(letra)
            precio_1[idx]=maximo
            max_1=max(precio_1)
            precio_2[idx]=maximo
            max_2=max(precio_2)
            print(f"El jugador {letra} ha reofertado { maximo}  para el bloque 1 y 2")
    elif josh == 20:
        if ofertado_0>max_0 and ofertado_2>max_2:
            maximo = max([ofertado_0,ofertado_2])
            idx=subastadores.index(letra)
            precio_0[idx]=maximo
            max_0=max(precio_0)
            precio_2[idx]=maximo
            max_2=max(precio_2)
            print(f"El jugador {letra} ha reofertado { maximo}  para el bloque 0 y 2")
    elif josh == 120 :
        if ofertado_0>max_0 and ofertado_2>max_2 and ofertado_1>max_1:
            maximo = max([ofertado_0,ofertado_2,ofertado_1])
            idx=subastadores.index(letra)
            precio_0[idx]=maximo
            max_0=max(precio_0)
            precio_2[idx]=maximo
            max_2=max(precio_2)
            precio_1[idx]=maximo
            max_1=max(precio_1)
            print(f"El jugador {letra} ha reofertado { maximo}  para el bloque 0, 1  y 2")
    #Esos print se pueden usar para verificar como cambia los valores q ofrece cada compañía por el servicio
    #print(precio_0)
    #print(precio_1)
    #print(precio_2)

async def main():
    await asyncio.gather(jugador('Telefonica'),jugador('Claro') ,jugador('Entel'))

if __name__ == "__main__":
    print("Bloques a subastar:")
    print("Bloque 0: 50MHz")
    print("Bloque 1: 60MHz")
    print("Bloque 2: 70MHz")
    print("Precio base de cada bloque 15 millones")
    for j in range(1,4):
        print(f"Ronda {j}")
        print(f"Bloque 0 : {max(precio_0)} millones")
        print(f"Bloque 1 : {max(precio_1)} millones")
        print(f"Bloque 2 : {max(precio_2)} millones")
        tic = time.perf_counter()
        while True:
            asyncio.run(main())
            toc=time.perf_counter()
            if toc-tic>=30:
                print(f"se cumplio el tiempo de 30 segundos. Ronda {j} finalizada")
                break
    idx =precio_0.index(max_0)
    ganador_0 = subastadores[idx]
    idx =precio_1.index(max_1)
    ganador_1 = subastadores[idx]
    idx =precio_2.index(max_2)
    ganador_2 = subastadores[idx]
    print ("Los ganadores son:")
    print(f"Bloque 0: {ganador_0} con $ {max_0} millones")
    print(f"Bloque 1: {ganador_1} con $ {max_1} millones")
    print(f"Bloque 2: {ganador_2} con $ {max_2} millones")
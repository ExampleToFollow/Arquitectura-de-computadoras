import asyncio
import time
import random
#Recomendacion ingresar un N= 10000000 aprox para q sea mayor al resto de los precios ofrecidos
subastadores = ['a','b','c','d','e','sniper']
precio = [20000,20000,20000,20000,20000,20000]
precio_min = max(precio)

async def jugador(letra):
    global precio_min 
    i = random.randint(0,10)
    await asyncio.sleep(i)
    ofertado = random.randint(precio_min+500 , int((1.2)*(precio_min+500)))
    if ofertado>precio_min:
        idx=subastadores.index(letra)
        precio[idx]=ofertado
        precio_min=max(precio)
        print(f"El jugador {letra} ha reofertado { ofertado}")

def jugador_sniper(letra):
    global precio_min
    ofertado = precio[5]
    idx=subastadores.index(letra)
    precio[idx]=ofertado
    precio_min=max(precio)
    print(f"El jugador {letra} ha reofertado { ofertado}")

async def main():
    await asyncio.gather(jugador('a'),jugador('b') ,jugador('c'),jugador('d'),jugador('e'))

def max(lista):
    max= 0
    for i in lista:
        if i>max:
            max=i
    return max

if __name__ == "__main__":
    tic= time.perf_counter()
    contador =0 
    while True:
        asyncio.run(main())
        toc=time.perf_counter()
        if toc-tic >=57 and contador == 0:
            archivo =open('oferta_del_sniper.txt','r')
            contenido = archivo.read()
            archivo.close()
            precio[5]=int(contenido)
            jugador_sniper('sniper')
            contador = contador +1

        if toc-tic >=60:
            print("se termino la subasta")
            print("Se cumplio el tiempo de 60 segundos")
            ganador_precio = max(precio)
            idx = precio.index(ganador_precio)
            ganador_letra = subastadores[idx]
            #print(subastadores)
            #print(precio)
            print(f"Ofertas finales son  {subastadores[0]} : {precio[0]} , {subastadores[1]}: { precio[1]} , {subastadores[2]}: {precio[2]} , { subastadores[3]} : {precio[3]}, {subastadores[4]}: {precio[4]} , {subastadores[5]}: {precio[5]} ")
            print(f"El ganador es {ganador_letra} con {ganador_precio}")
            break

##el archivo cliente y server son parte de esta pregunta durante los 56 primeros segundos se debe ingresar un valor en el teminal del cliente para q el servidor cree el archivo txt
import asyncio
import time
import random
subastadores = ['a','b','c','d','e']
precio = [20000,20000,20000,20000,20000]
precio_min = max(precio)
async def jugador(letra):
    global precio_min 
    i = random.randint(1,11)
    await asyncio.sleep(i)
    ofertado = random.randint(precio_min+500 , int((1.2)*(precio_min+500)))
    if ofertado>=precio_min:
        idx=subastadores.index(letra)
        precio[idx]=ofertado
        #precio_min=ofertado
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
    while True:
        asyncio.run(main())
        toc=time.perf_counter()
        if toc-tic >=20:
            print("se termino la subasta")
            ganador_precio = max(precio)
            idx = precio.index(ganador_precio)
            ganador_letra = subastadores[idx]
            print(subastadores)
            print(precio)
            print(f"El ganador es {ganador_letra} con {ganador_precio}")
            break
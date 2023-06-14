import random
import asyncio
subastadores= ['telefonica','claro','entel']
precio_0 = [15,15,15]
letra_0= ['','','']
precio_1 = [15,15,15]
letra_1= ['','','']
precio_2 = [15,15,15]
letra_2= ['','','']

def max(lista):
    max= 0
    for i in lista:
        if i>max:
            max=i
    return max
#async with asyncio.timeout(60): da vida de 60 segundos
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


if __name__ == "__main__":
    print("Bloques a subastar:")
    print("Bloque 0: 50MHz")
    print("Bloque 1: 60MHz")
    print("Bloque 2: 70MHz")
    print("Precio base de cada bloque 15 millones")
    for j in range(1,4):
        print(f"Ronda {j}")
        print(f"Bloque 0 : {max(precio_0)}millones")
        print(f"Bloque 1 : {precio_1}millones")
        print(f"Bloque 2 : {precio_2}millones")
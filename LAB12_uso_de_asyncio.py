import time
import asyncio
import random

PRECIO_MINIMO = 20000   #El precio base al que se inicia la subasta
PRECIO_MAXIMO = 100000  #El precio maximo que cualquiera de los participantes está dispuesto a pagar(úselo como tope en random.randint()

async def jugador(lista_numero, lista_letra ,letra):
    i = random.randint(0,10)
    await asyncio.sleep(i)
    ofertado = random.randint(PRECIO_MINIMO,PRECIO_MAXIMO)
    lista_numero.append(ofertado)
    lista_letra.append(letra)

def max(lista):
    max= 0
    for i in lista:
        if i>max:
            max=i
    idx = lista.index(max)
    return max , idx

async def main(lista_numero, lista_letra):
    await asyncio.gather(jugador(lista_numero ,lista_letra ,'a'),jugador(lista_numero ,lista_letra ,'b'),jugador(lista_numero ,lista_letra ,'c'),jugador(lista_numero ,lista_letra ,'d'),jugador(lista_numero ,lista_letra ,'e'))

if __name__ == "__main__":
    lista_numero=[]
    lista_letra = []
    asyncio.run(main(lista_numero, lista_letra))
    print(lista_letra)
    print(lista_numero)
    aux = max(lista_numero)  
    print(f"Ofertas finales:(  {lista_letra[0]} : {lista_numero[0]} , {lista_letra[1]} : {lista_numero[1]} , {lista_letra[2]} : {lista_numero[2]} , {lista_letra[3]} : {lista_numero[3]} , {lista_letra[4]} : {lista_numero[4]} )")
    print(f"El ganador es:' { lista_letra[aux[1]]} ' ")
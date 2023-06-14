import asyncio
import random
async def jugador(lista_numero, lista_letra ,letra):
    precio_min = 20000
    i = random.randint(1,11)
    await asyncio.sleep(i)
    ofertado = precio_min+random.randint(1000,50000)
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
    print(f"Ofertas finales:  {lista_letra[0]} : {lista_numero[0]} ,{lista_letra[1]} : {lista_numero[1]} ,{lista_letra[2]} : {lista_numero[2]} ,{lista_letra[3]} : {lista_numero[3]} ,{lista_letra[4]} : {lista_numero[4]} ")
    print(f"El ganador es: { lista_letra[aux[1]]} ")








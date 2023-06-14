import asyncio
import time
import random
import socket 
SOCKET_BUFFER = 1024

subastadores = ['a','b','c','d','e','sniper']
precio = [20000,20000,20000,20000,20000,20000]
precio_min = max(precio)

async def jugador(letra):
    global precio_min 
    i = random.randint(1,11)
    await asyncio.sleep(i)
    ofertado = random.randint(precio_min+500 , int((1.2)*(precio_min+500)))
    if ofertado>=precio_min:
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
    msg = input("> ")
    sock = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
    server_address = ('192.168.56.1',5000)
    sock.connect(server_address) 
    sock.sendall(msg.encode())
    sock.close()
    tic= time.perf_counter()
    contador =0 
    while True:
        asyncio.run(main())
        toc=time.perf_counter()
        if toc-tic >=40 and contador == 0:
            archivo =open('oferta_del_sniper.txt','r')
            contenido = archivo.read()
            archivo.close()
            precio[5]=int(contenido)
            jugador_sniper('sniper')
            contador = contador +1

        if toc-tic >=50:
            print("se termino la subasta")
            ganador_precio = max(precio)
            idx = precio.index(ganador_precio)
            ganador_letra = subastadores[idx]
            print(subastadores)
            print(precio)
            print(f"El ganador es {ganador_letra} con {ganador_precio}")
            break
            

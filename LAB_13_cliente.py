import socket
import threading 
import time
SOCKET_BUFFER = 1024
def recibir():
    global contenido
    while True:
            msg = sock.recv(SOCKET_BUFFER)
            msg = msg.decode()
            #print("ola")
            if (msg != 'stop'):
                #print(msg)
                contenido.append(msg)
            else:
                break
#ID;Nombre;N�mero de parte;Cantidades;Peso(g);Costo unitario($)
def clasifica(precio):
    precio = int(precio)
    if precio<25 :
        return 'Costo bajo'
    elif precio>=25 and precio<=49.9:
        return 'Costo regular'
    elif precio>=50 and precio<=74.9:
        return 'Costo alto'
    elif precio>=75:
        return 'Costo elevado'

def imprimir(nombre, costo_total,  clasificacion, num_costo_elevado,num_costo_elevado_bajo_peso, num_costo_bajo):
    print(f"--------------Nombre: {nombre}--------------")
    print(f"Costo total: {costo_total}")
    print(f"Clasificacion por costo : {clasificacion}")
    print(f"Numero de componentes con costo elevado: {num_costo_elevado}")
    print(f"Numero de componentes con costo elevado y con peso mayor a 100g: {num_costo_elevado_bajo_peso}")
    print(f"Numero de componentes con costo bajo: {num_costo_bajo}")

def procesa_datos():
    time.sleep(3)
    global contenido
    counter_costo_elevado = 0
    counter_costo_elevado_bajo_peso = 0
    counter_costo_bajo = 0
    lista_costo=[]
    #ID;Nombre;N�mero de parte;Cantidades;Peso(g);Costo unitario($)
    for j in contenido[1::]:
        lista = j.split(";")
        #print(lista)
        cantidad=int(lista[3])
        peso=int(lista[4])
        costo=float(lista[5])
        costo_total = cantidad*costo
        lista_costo.append(costo_total)
        clasificacion=clasifica(costo_total)
        if clasificacion == 'Costo elevado':
            counter_costo_elevado = counter_costo_elevado+1 
            if peso>100:
                counter_costo_elevado_bajo_peso=counter_costo_elevado_bajo_peso+1
        elif clasificacion == 'Costo bajo':
            counter_costo_bajo =counter_costo_bajo+1
        imprimir(lista[1],costo_total,clasificacion,counter_costo_elevado,counter_costo_elevado_bajo_peso,counter_costo_bajo)
        time.sleep(0.1)
if __name__ == "__main__":
    contenido =[]
    Thread_1= threading.Thread(target=recibir , args=())
    Thread_2= threading.Thread(target=procesa_datos ,args=())
    sock = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
    server_address= ('localhost', 5000)
    print(f" Conectando al IP : {server_address[0]} y puerto {server_address[1]}")

    try:
        sock.connect(server_address)
        Thread_1.start()
        Thread_2.start()
        Thread_1.join()
        Thread_2.join()
        
    except ConnectionRefusedError:
        print("No se pudo conectar al servidor")
    except KeyboardInterrupt:
        sock.close()
    finally:
        sock.close()
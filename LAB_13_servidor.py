import threading 
import time
import socket
contenido = ''
def read_csv():
    global contenido
    with open('PartesDeElectrónica.csv', "r") as f:
        arch = f.read()
    #print(arch)
    #print(type(arch))
    contenido = arch
        
def send_client ():
    time.sleep(2)
    global contenido
    contenido =str(contenido)
    lista = contenido.split("\n")
    for i in lista:
        msg = i.encode()
        connection.sendall(msg) 
        time.sleep(0.001)
    a='stop'
    connection.sendall(a.encode())


if __name__ == "__main__":
    contenido = 0
    thread_1 = threading.Thread(target = read_csv , args = () )
    thread_2 = threading.Thread(target = send_client , args = ())
    SOCKET_BUFFER = 1024
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    print(f"Iniciando servidor en IP {server_address[0]}, con puerto {server_address[1]}")
    sock.bind(server_address)
    sock.listen(1)
    print("Esperando la coneccion de un cliente")
    connection,  client_address = sock.accept()
    print(f"Iniciando conecciones {client_address[0] } y puerto { client_address[1]}")
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    connection.close()
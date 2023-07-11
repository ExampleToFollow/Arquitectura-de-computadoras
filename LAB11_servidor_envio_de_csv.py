import socket
import numpy as np
import time
def abrir_csv():
    with open("pacientes.csv", "r") as f:
        contenido = f.read()
    #print((contenido))
    filas = contenido.split("\n")
    #print(len(filas))
    return filas 

if __name__ == "__main__":
    SOCKET_BUFFER = 1024
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("192.168.35.139", 5025)
    print(f"Iniciando servidor en IP {server_address[0]}, con puerto {server_address[1]}")
    sock.bind(server_address)
    sock.listen(1)
    while True:
        print("Esperando la coneccion de un cliente")
        connection,  client_address = sock.accept()
        print(f"Iniciando conecciones {client_address[0] } y puerto { client_address[1]}")
        data  = connection.recv(SOCKET_BUFFER).decode()
        if data != "2":
            try:
                with open("pacientes.csv","a") as f:
                    f.write("\n"+ data)
                    
                with open("pacientes.csv", "r") as f:
                    contenido = f.read()
            finally:
                pass
        if data == "2":
            while True:
                filas = abrir_csv()
                #long = len(filas) 
                try: 
                    for i in filas:
                        connection.sendall(i.encode())
                        time.sleep(0.1)
                    connection.sendall("no".encode())  
                except BrokenPipeError:
                    pass
                    connection.close()

                #vamos a enviar 30 lineas a la vez
                #enviar.encode("utf-8")
                #print(type(enviar))
                #connection.sendall(enviar.encode())
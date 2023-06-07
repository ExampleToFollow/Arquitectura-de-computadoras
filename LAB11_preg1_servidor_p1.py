import socket
import time
if __name__ == "__main__":
    SOCKET_BUFFER = 1024

    #funciona como cliente
    sock_master = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server_master_address = ('192.168.56.1', 5010) 
    sock_master.connect(server_master_address)
    #pero también como servidor
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server_address = ('192.168.56.1', 5021)
    sock.bind(server_address)
    sock.listen(1)
    print("Esperando clientes")
    while True:
        try :
            connection, client_address = sock.accept()
            #Actua como cliente
            while True:
                
                    print(f"Cliente se conecta desde {client_address[0]} y {client_address[1]}")
                    frase = sock_master.recv(SOCKET_BUFFER)
                    frase= frase.decode()
                    lon = str(len(frase))
                    print(f"HOLA SOY SERVIDOR Y HE RECIBIDO DE MASTER {len(frase)} bytes : {frase}")
                    connection.sendall(lon.encode())
                    time.sleep(1)
        except KeyboardInterrupt:
            break
        except ConnectionResetError:
            print("El servidor se cerró")
        except ConnectionAbortedError:
            print("El servidor anulo la sesion")


                
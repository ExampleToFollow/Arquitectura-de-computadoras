import socket 

SOCK_BUFFER = 1024

if __name__  == '__main__' : 
    sock  = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
    server_address = ("0.0.0.0" , 5000)
    print(f"Iniciando el servidor en IP {server_address[0]} , con puerto {server_address[1]}")
    sock.bind(server_address)

    sock.listen(5)

    print("Esperando conexiones")

    while True : 
        try : 
            conn ,client_address = sock.accept()
            print(f"Conexion entrante de  ('{client_address[0]}' , '{client_address[1]}')") 
        except KeyboardInterrupt:
            print("Cerrando el servidor ...")
            break
        finally:
            conn.close()
    sock.close()
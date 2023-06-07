import socket

if __name__ == "__main__":
    SOCKET_BUFFER = 1024
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("192.168.56.1", 5030)
    print(f"Iniciando servidor en IP {server_address[0]}, con puerto {server_address[1]}")
    sock.bind(server_address)
    sock.listen(1)
    while True:
        print("Esperando la coneccion de un cliente")

        connection,  client_address = sock.accept()
        print(f"Iniciando conecciones {client_address[0] } y puerto { client_address[1]}")
        data  = connection.recv(SOCKET_BUFFER).decode()
        try:
            with open("pacientes.csv","a") as f:
                f.write("\n"+ data)
                
            with open("pacientes.csv", "r") as f:
                contenido = f.read()
            
            print(contenido)
                #contenido = f.read()
              #  print (contenido)
             #   contenido = contenido + f"\n{data}"
            #with open("pacientes.csv","w+") as f:
            #    f.write(contenido)
        finally:
            pass
        


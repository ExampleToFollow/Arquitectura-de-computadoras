import socket
import time
def abrir_txt():
    with open("c:\\Users\\Hineill\\Desktop\\5TO CICLO\\ARQUITECTURA DE COMPUTADORAS\\.vscode\\LAB11\\pregunta1.txt", "r") as f:
        contenido = f.read()
    filas = contenido.split("\n")
    return filas 

if __name__ == "__main__":
    SOCKET_BUFFER = 1024
    filas = abrir_txt()
    #print(type(filas[0])) # 5016 elementos
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 5010)
    sock.bind(server_address)
    sock.listen(1)
   
    print("Esperando conexiones...")
    conn , client_address = sock.accept()
    print(f"Conexion desde  : {client_address[0]}: {client_address[1]}")
    while True:
        for i in filas:
            try:
                data = i
                data = data.encode()
                conn.sendall(data)
                time.sleep(1)
            #except ConnectionResetError:
            #    print("El cliente se desconecto")
            #    print("Esperando al cliente de nuevo...")
            #    conn , client_address = sock.accept()
            #    data = i
            #    data = data.encode()
            #    conn.sendall(data)
            #    time.sleep(1)
            except ConnectionAbortedError :
                print("El cliente se desconecto")
                print("Esperando al cliente de nuevo...")
                conn , client_address = sock.accept()
                data = i
                data = data.encode()
                conn.sendall(data)
                time.sleep(1)
            except KeyboardInterrupt:
                conn.close()

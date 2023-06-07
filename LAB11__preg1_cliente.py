import socket
if __name__ == "__main__":
    SOCKET_BUFFER = 1024
    sock = socket.socket(socket.AF_INET ,  socket.SOCK_STREAM)
    server_address = ('192.168.56.1', 5021)
    sock.connect(server_address)
    while True:
        try:
            msg= sock.recv(SOCKET_BUFFER)
            msg = msg.decode()
            print(f"HOLA SOY CLIENTE Y LA CANTIDAD DE CARACTERES RECIBIDA POR SERVIDOR ES : {msg}")
        except ConnectionError:
            print("No se conecto al server")
        except OSError:
            pass  
            msg= sock.recv(SOCKET_BUFFER)
            msg = msg.decode()
            print(f"HOLA SOY CLIENTE Y LA CANTIDAD DE CARACTERES RECIBIDA POR SERVIDOR ES : {msg}")
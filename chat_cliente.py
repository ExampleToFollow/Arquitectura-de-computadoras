import socket

def main():
    SOCKET_BUFFER = 1024
    cliente_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server_address = ("192.168.35.131" , 5000)
    cliente_socket.connect(server_address)

    try: 
        while True: 
            print("Esperando mensaje del servidor ...")
            print("servidor : " , cliente_socket.recv(1024).decode())
            mensaje = cliente_socket.recv(1024).decode()
            if mensaje.lower() == "salir":
                break
            print(">")
            ingresado = input()
            cliente_socket.sendall(ingresado.encode())
            if cliente_socket.lower()=="salir":
                break
    finally:
        cliente_socket.close()
        


if __name__ == "__main__":
    main()
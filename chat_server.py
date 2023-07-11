import socket

def main():
    SOCKET_BUFFER = 1024
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5000))
    server_socket.listen(1)
    print("El servidor está escuchando en el puerto 5000...")

    # Aceptar la conexión del cliente
    cliente_socket, cliente_address = server_socket.accept()
    print("Cliente conectado:", cliente_address)
    try:
        while True:
            print(">")
            ingresado = input()
            cliente_socket.sendall(ingresado.encode())
            if ingresado.lower()=="salir":
                break
            print("Esperando respuesta")
            mensaje = cliente_socket.recv(1024).decode()
            print(f"Cliente: {mensaje} .")
            if mensaje.lower() == "salir":
                break
    finally:
        cliente_socket.close()
        server_socket.close()


if __name__ == "__main__":
    main()

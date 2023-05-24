import socket

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.56.1', 5000))
    print("Conectado al servidor.")
    while True:
        # Turno del servidor
        print("Esperando mensaje del servidor...")
        server_message = client_socket.recv(1024).decode()
        print("Servidor:", server_message)

        # Verificar si se debe cerrar la conexión
        if server_message.lower() == "salir":
            break

        # Turno del cliente
        print(">")
        message = input()
        client_socket.send(message.encode())

        # Verificar si se debe cerrar la conexión
        if message.lower() == "salir":
            break

    # Cerrar la conexión
    client_socket.close()
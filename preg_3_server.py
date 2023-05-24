import socket

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5000))
    server_socket.listen(5)
    print("El servidor está escuchando en el puerto 5000...")

    # Aceptar la conexión del cliente
    client_socket, client_address = server_socket.accept()
    print("Cliente conectado:", client_address)

    while True:
        # Turno del servidor
        print(">")
        message = input()
        client_socket.send(message.encode())

        # Verificar si se debe cerrar la conexión
        if message.lower() == "salir":
            break

        # Turno del cliente
        print("Esperando respuesta del cliente...")
        client_message = client_socket.recv(1024).decode()
        print("Cliente:", client_message)

        # Verificar si se debe cerrar la conexión
        if client_message.lower() == "salir":
            break

    # Cerrar la conexión
    client_socket.close()
    server_socket.close()

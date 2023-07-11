import socket
SOCKET_BUFFER = 1024

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
    server_address= ('192.168.35.139', 5000)
    print(f" Conectando al IP : {server_address[0]} y puerto {server_address[1]}")

    try:
        sock.connect(server_address)
        msg = []
        print("Ingrese datos del paciente")
        msg.append(input(">Nombre(s): "))
        msg.append(input(">Apellidos: "))
        msg.append(input(">Peso(kg): "))
        msg.append(input(">Talla(cm): "))
        msg.append(input(">Edad: "))
        seguro = input(">Cuenta con seguro? (s/n): ")
        if seguro == "s":
            msg.append("True")
        else:
            msg.append("False")
        enviar = ""
        for i in msg[:-1]:
            enviar = enviar + i + " , "
        
        enviar = enviar + msg[-1]
        enviar = enviar.encode()
        sock.sendall(enviar)
        print("Enviando al servidor...")
    except ConnectionRefusedError:
        print("No se pudo conectar al servidor")
    finally:
        sock.close()
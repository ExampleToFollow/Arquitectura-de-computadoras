import socket
SOCKET_BUFFER = 1024
import time
if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
    server_address= ('192.168.35.139', 5025)
    print(f" Conectando al IP : {server_address[0]} y puerto {server_address[1]}")

    try:
        sock.connect(server_address)
        msg = []
        print("¿Que desea hacer")
        print("1: Ingresar paciente")
        print("2: descargar pacientes")
        entrada = input("> ")
        if entrada == "1" :
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
                enviar = enviar + i + ","
            
            enviar = enviar + msg[-1]
            enviar = enviar.encode()
            sock.sendall(enviar)
        
        if entrada == "2":
            sock.sendall(entrada.encode())
            tic = time.perf_counter()
            while True:
                download = sock.recv(SOCKET_BUFFER)
                if download.decode() != "no":
                    download = download.decode()
                    print(download)
                    with open("pregunta_2.txt","a") as f:
                        f.write(download)
                        f.write("\n")
                else:
                    break 
            toc = time.perf_counter()
            lon = len(download)
            velocidad = (lon/(toc-tic))*(10**(-6))
            #La velocidad de descarga es muy baja debido a que estamos enviando linea por linea
            print(f"Velocidad de descarga: {velocidad} MB/s")
            #print(download)
    except ConnectionRefusedError:
        print("No se pudo conectar al servidor")
    finally:
        sock.close()
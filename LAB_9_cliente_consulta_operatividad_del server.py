import socket
#con esta libreria aseguraremos que el cliente intente acceder al servidor cada 5 segundos
import time
from colorama import init , Fore
init()
def main():
    SOCK_BUFFER = 1024
    while True:
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        server_address = ("192.168.35.131", 5000)
        try:
            #sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            #server_address = ("192.168.35.131", 5000)
            sock.connect(server_address)
            print(Fore.GREEN + "[*] El servidor está operativo")
        except:
            print(Fore.RED + "[-] El servidor no responde")
        finally:
            sock.close()
            time.sleep(5)
    


if __name__ == "__main__":
    main()
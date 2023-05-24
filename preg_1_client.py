import socket
import time
from colorama  import init , Fore
init ()
SOCK_BUFFER = 1024
if __name__ == '__main__':
    while True :
        try : 
            sock = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
            server_address = ("192.168.56.1", 5000)
            sock.connect(server_address)
            print(Fore.GREEN + "[*]El servidor está operativo")
        except:
            print(Fore.RED + "[-] El servidor no funciona Auxilio")
        finally:
            sock.close()
            time.sleep(5)
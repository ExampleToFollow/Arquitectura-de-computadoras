import socket 
import sys

if __name__ == "__main__":
    ip = sys.argv[1]
    rango = range(101)
    for i in rango[1:101]:
        try:
            sock= socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((ip, i))
            print(f"Puerto { i } está abierto")
        except TimeoutError:
            pass
        finally:
            sock.close()

    
        
    
    

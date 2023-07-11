import socket
#import time
 
def main():
    SOCK_BUFFER = 1024
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("0.0.0.0" , 5000)
    print("Esperando conexiones ...")
    sock.bind(server_address)
    sock.listen(5)
    while True :
        try : 
            soc , cliente_address = sock.accept()
            print(f"Conexion entrante de (' {cliente_address[0]} ' , ' {cliente_address[1]}' )")
        
        except KeyboardInterrupt :
            print("Cerrando el servidor... :c")
            break
        finally:
            soc.close()
    sock.close()

if __name__ == "__main__":
    main()
        

import socket

if __name__ == "__main__":
    SOCKET_BUFFER= 1024
    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address= ('192.168.122.1', 5000)
    sock.bind(server_address)
    sock.listen(1)
    print("Esperando clientes")
    try:
        connection, client_address = sock.accept()
        print(f"Cliente se conecta desde {client_address[0]} y {client_address[1]}")
        msg = connection.recv(SOCKET_BUFFER)
        msg = msg.decode()
        archivo = open('oferta_del_sniper.txt','w')
        archivo.write(msg)
        connection.close()
    finally:
        sock.close()
import socket
SOCKET_BUFFER = 1024
if __name__ == "__main__":
    msg = input("> ")
    sock = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
    server_address = ('192.168.122.1',5000)
    sock.connect(server_address) 
    sock.sendall(msg.encode())
    sock.close()
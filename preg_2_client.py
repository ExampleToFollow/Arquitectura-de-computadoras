import pickle 
import socket
import numpy as np

SOCK_BUFFER = 1024
if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
    server_address = ("192.168.56.1", 5000)
    sock.connect(server_address)
    try : 
        mat_1 = [[4 , 4] , [ 1 , 1]]
        mat_2 = [[4 , 4] , [ 1 , 1]]
        data = [mat_1 ,  mat_2]
        sock.sendall(pickle.dumps(data))
        mat_res = sock.recv(SOCK_BUFFER)
        mat_res = pickle.loads(mat_res)
        print(f"Producto es  : \n {mat_res}") 
    except ConnectionResetError:
        pass
    finally:
        sock.close()
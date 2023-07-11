import socket
import pickle
import numpy as np
#np.random
def main():
    SOCK_BUFFER = 1024
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server_address = ("192.168.35.131", 5000)
    sock.connect(server_address)
    try:
        #creamos las matrices y las ponemos en un arreglo
        N = 2  
        mat_1 = [ [np.random.randint(1,10) for j in range(2)] for  i in range(2)] 
        mat_2 = [ [np.random.randint(1,10) for j in range(2)] for  i in range(2)] 
        #mat_1 =[[1,1], [1,1]]
        #mat_2 = [[1,1],[1,1]]
        message = [mat_1, mat_2]
        #enviamos el mensaje serializado
        sock.sendall(pickle.dumps(message))
        
        #recibimos la respuesta del calculo del server
        product_matrix = sock.recv(SOCK_BUFFER)
        #deserializamos a el dato enviado por el server
        product_matrix = pickle.loads(product_matrix) 
        print("Producto de las matrices es ")
        print(product_matrix)

    except ConnectionResetError:
        pass
    finally:
        sock.close()
        

if __name__ == "__main__":
    main()

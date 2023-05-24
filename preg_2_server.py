import socket 
import pickle 
import numpy as np
SOCK_BUFFER = 1024

if __name__  == '__main__' : 
    sock  = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
    server_address = ("0.0.0.0" , 5000)
    sock.bind(server_address)
    sock.listen(5)
    print("Esperando conexiones...")
    while True : 
        try : 
            conn ,client_address = sock.accept()
            print(f"Conexion entrante de  ('{client_address[0]}' , '{client_address[1]}')") 
            while True:
                data = conn.recv(SOCK_BUFFER)
                if data: 
                    mat = pickle.loads(data)
                    mat_1 = mat[0]
                    mat_2 = mat[1]
                    mat_res = np.dot(np.array(mat_1) ,np.array(mat_2))
                    conn.sendall(pickle.dumps(mat_res))
                else:
                    break
        except KeyboardInterrupt:
            print("Cerrando el servidor")
            break
        finally:
            conn.close()
    sock.close()
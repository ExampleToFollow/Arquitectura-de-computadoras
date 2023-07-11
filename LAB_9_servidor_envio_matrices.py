import numpy as np
import socket
import pickle
def main():
    SOCK_BUFFER = 1024
    sock =socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server_address = ("0.0.0.0" ,5000)
    sock.bind(server_address)
    sock.listen(1)
    print("Esperando conexiones")
    while True:
        try:
            soc, client_address = sock.accept()
            print(f"Conexion entrante de ('{client_address[0] }', '{client_address[1]}')")
            matrix = soc.recv(SOCK_BUFFER)
            matrix = pickle.loads(matrix)
            rpta = np.dot(np.array(matrix[0]), np.array(matrix[1]))
            soc.sendall(pickle.dumps(rpta))
        except KeyboardInterrupt:
            print("Cerrando el servidor")
        finally:
            soc.close()

    sock.close()

if __name__ == "__main__":
    main()



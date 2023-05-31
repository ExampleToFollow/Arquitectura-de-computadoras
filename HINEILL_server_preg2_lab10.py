import socket, pickle
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    SOCKET_BUFFER= 4248
    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address= ('192.168.56.1', 5001)
    sock.bind(server_address)
    sock.listen(1)
    print("Esperando clientes")

    try:
        #while True:
            #try:
                connection, client_address = sock.accept()
                print(f"Cliente se conecta desde {client_address[0]} y {client_address[1]}")
                #recibimos la imagen del cliente
                image = connection.recv(SOCKET_BUFFER)
                image = pickle.loads(image)
                #para generar la nueva imagen
                for i in range(64):
                    for j in range(64):
                        image[i][j]= 255- image[i][j]
                negative_image =image
                #enviamos la imagen alterada
                negative_image = pickle.dumps(negative_image)
                connection.sendall(negative_image)
                print("Imagen enviada")
                connection.close()
            #except TimeoutError:
             #   pass
    except KeyboardInterrupt:
        sock.close()




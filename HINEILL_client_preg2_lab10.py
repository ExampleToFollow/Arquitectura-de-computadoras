import socket
import matplotlib.pyplot as plt
import pickle
import time
import numpy as np


def guardar_imagen_como_png(img_array):	
	plt.imshow(img_array, cmap='gray')
	plt.axis('off')
	plt.savefig('imagen_en_negativo.png', bbox_inches='tight')

if __name__ == "__main__":
	#decidimos este buffer por el tamaño de la imagen en bits
    SOCKET_BUFFER = 4248
    tic_load = time.perf_counter()
    image = np.load('lena_64x64.npy')
    toc_load = time.perf_counter()
    #time_load = (toc-tic)
    try:
        sock = socket. socket(socket.AF_INET , socket.SOCK_STREAM)
        server_address = ('192.168.56.1', 5001) 
        sock.connect(server_address)
        #se envia la imagen
        tic_wait= time.perf_counter()
        image = pickle.dumps(image)
        sock.sendall(image)
        #se recibe la imagen alterada
        negative_image = sock.recv(SOCKET_BUFFER)
        negative_image = pickle.loads(negative_image)
        toc_wait= time.perf_counter()
        guardar_imagen_como_png(negative_image)
        #time_wait = (toc-tic)*(10**4)
        print(f"El tiempo empleado en cargar la imagen del disco a la RAM fue de {toc_load-tic_load}")
        print(f"El tiempo empleado en enviar y recibir la imagen negada fue de {toc_wait-tic_wait}")
        print("Entonces")
        if (toc_wait-tic_wait > toc_load-tic_load):
             print("El tiempo de envio y recibo de la imagen demoró más que el tiempo de carga de la imagen")
        else:
             print("El tiempo de carga de la imagen demoró más que el tiempo de envio y recibo de la imagen")
    except ConnectionRefusedError:
         print("No se conectó al server")
    finally:
         #guardar_imagen_como_png(negative_image)
         sock.close()
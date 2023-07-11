import socket
import numpy as np
import matplotlib.pyplot as plt
import pickle 
import time
def guardar_imagen_como_png(img_array):
	plt.imshow(img_array, cmap='gray')
	plt.axis('off')
	plt.savefig('imagen_en_negativo.png', bbox_inches='tight')


if __name__ == "__main__":
	#decidimos este buffer por el tamaño de la imagen en bytes
    SOCKET_BUFFER = 8192
    tic_load = time.perf_counter()
    image = np.load('lena_64x64.npy')
    toc_load = time.perf_counter()
    try:
        sock = socket. socket(socket.AF_INET , socket.SOCK_STREAM)
        server_address = ('192.168.35.140', 5000) 
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
        print(f"El tiempo empleado en cargar la imagen del disco a la RAM fue de {toc_load-tic_load}")
        print(f"El tiempo empleado en enviar y recibir la imagen negada fue de {toc_wait-tic_wait}")
        print("Entonces")
        #el mismo programa imprimé cual es la acción q demora más en ejecutarse
        if (toc_wait-tic_wait > toc_load-tic_load):
             print("El tiempo de envio y recibo de la imagen demoró más que el tiempo de carga de la imagen")
        else:
             print("El tiempo de carga de la imagen demoró más que el tiempo de envio y recibo de la imagen")
    except ConnectionRefusedError:
         print("No se conectó al server")
    finally:
         sock.close()
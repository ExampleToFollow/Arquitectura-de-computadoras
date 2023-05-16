import sys
import numpy as np

direccion_ip = sys.argv[1] #Ejm: 192.168.10.31
mascara_cidr = int(sys.argv[2]) #Ejm: 16

#1) Convertir la direccion IP y la mascara a formato binario
octetos = direccion_ip.split(".") #Corta una cadena de texto de acuerdo al caracter separador que se especifique y los resultados los almacena en una lista
octetos_binarios = ""
for octeto in octetos:
    octetos_binarios += bin(int(octeto))[2:].zfill(8) #zfill completa de ceros hasta que lleguemos a la cantidad de caracteres especificados

mascara_binaria = "1" * mascara_cidr + "0" * (32 - mascara_cidr)

#2) Obtener la direccion de red en binario con la operacion AND entre la direccion IP y la mascara
red_binaria = ""
for bit1, bit2 in zip(octetos_binarios,mascara_binaria): #Recibe como parametros 2 listas o cadenas de igual dimension y forma una lista de pares donde cada par seran los elementos n-esimos de cada lista
    red_binaria += str(int(bit1) and int(bit2))

#3) Convertir la direccion de red a formato de octetos decimales
red = ""
for i in range(0, 32, 8):
    red += str(int(red_binaria[i:i+8], 2))
    if (i<24):
        red += "."

print("La dirección IP es:", direccion_ip)
print("La máscara de subred en notación CIDR es:", mascara_cidr)
print("La dirección de red correspondiente es:", red)

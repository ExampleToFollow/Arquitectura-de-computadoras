#!/usr/bin/env python
from socket import AF_INET, SOCK_DGRAM
import datetime
import threading
import socket
import struct
import time
servidores_ntp = [
	"0.uk.pool.ntp.org",    # Londres(Reino Unido)
	"1.es.pool.ntp.org",    # Madrid (España)
	"0.us.pool.ntp.org",    # Nueva York(Estados Unidos)
	"0.hk.pool.ntp.org",    # Hong Kong
	"0.jp.pool.ntp.org"     # Tokyo(Japón)
]

"""
Función: get_ntp_time
Descripción: Imprime la  fecha-hora actual en un país determinado
Entrada: Cualquiera de las URLs definidas en la lista servidores_ntp
Salida: Retorna la fecha-hora(timestamp) en formato datetime.datetime, también la imprime
IMPORTANTE: NO modifique esta funcion 
"""
def get_ntp_time(host):
	timezone_dict = {'uk': ['UK', 0 * 3600], 'es': ['España', 1 * 3600],
	                 'hk': ['Hong Kong', 8 * 3600], 'jp': ['Japón', 9 * 3600],
	                 'us': ['Estados Unidos', -5*3600]}
	key = ''
	port = 123
	buf = 1024
	address = (host, port)
	msg = b'\x1b' + 47 * b'\0'

	# reference time (in seconds since 1900-01-01 00:00:00)
	TIME1970 = 2208988800  # 1970-01-01 00:00:00
	# connect to server
	client = socket.socket(AF_INET, SOCK_DGRAM)
	client.sendto(msg, address)
	msg, address = client.recvfrom(buf)
	t = struct.unpack("!12I", msg)[10]
	t -= TIME1970
	client.close()

	for each_key in timezone_dict:
		if each_key in host:
			key = each_key
			break
	print(f"Hora en {timezone_dict[key][0]}: {datetime.datetime.utcfromtimestamp(t + timezone_dict[key][1])}")
	return datetime.datetime.utcfromtimestamp(t + timezone_dict[key][1])


paises = ['UK' , 'ESPAÑA' , 'EEUU','HONG KONG', 'JAPON']
def itera():
	global paises
	lista = []
	lista_hour = []
	#lista_minute = []
	#lista_second = []
	for i in servidores_ntp:
		lista.append(get_ntp_time(i))
		idx = servidores_ntp.index(i)
		lista_hour.append(lista[idx].hour)
		#lista_minute.append(lista[idx].minute)
	#print(lista)
	#print(lista_hour)
	restas=[]
	for i in lista_hour:
		rest = 8-i
		#en caso la hora sea menor a las 8, debemos calcular el tiempo que falta para las 8 am de ESE día
		if rest>=0:
			restas.append(rest)
		#en caso la hora sea mayor a las 8, el rest saldra negativo y tendrá que calcular el tiempo q le falta para las 8am del día siguiente
		#dicho tiempo faltante se puede calcular como rest(numero negativo) +  24 
		elif rest<0:
			rest = 24+rest
			#se agrega cada valor de tiempo a una lista
			restas.append(rest)
	min =26
	for i in restas:
		if i<min:
			min=i
	inde = restas.index(min)
	print(f"EL país que está más cercano a abrir su bolsa de valores es  {paises[inde]}")

aux=[] 
aux_2=[]
def itera_thread(pais):
	global aux ,aux_2
	horario = get_ntp_time(pais)
	horario = horario.hour
	resta = 8-horario 
	if resta>=0:
		aux.append(resta)
	elif resta<0:
		resta = 24+resta
		aux.append(resta)
	idx = servidores_ntp.index(pais)
	aux_2.append(paises[idx])

def elegir_menor(lista_1):
	menor=26
	for i in lista_1:
		if i<menor:
			menor=i
	return menor
if __name__ == '__main__':
	print("Parte_a) SIN THREADS")
	tic =time.perf_counter()
	itera()
	toc = time.perf_counter()
	tiempo_1 = toc-tic
	print(f"El tiempo de ejecucion de la funcion sin threads fue {tiempo_1}") 
	print("Parte_b) CON THREADS")
	Thread_0= threading.Thread(target= itera_thread , args = (servidores_ntp[0],))
	Thread_1= threading.Thread(target= itera_thread , args = (servidores_ntp[1],))
	Thread_2= threading.Thread(target= itera_thread , args = (servidores_ntp[2],))
	Thread_3= threading.Thread(target= itera_thread , args = (servidores_ntp[3],))
	Thread_4= threading.Thread(target= itera_thread , args = (servidores_ntp[4],))

	tic = time.perf_counter()
	Thread_0.start()
	Thread_1.start()
	Thread_2.start()
	Thread_3.start()
	Thread_4.start()
	Thread_0.join()
	Thread_1.join()
	Thread_2.join()
	Thread_3.join()
	Thread_4.join()
	menor = elegir_menor(aux)
	indice = aux.index(menor)
	#print(indice)
	#con esto nos aseguramos que sea el indice de la lista donde fuimos guardando cada elemento
	print(f"EL pais que está más cerca a abrir la bolsa de valores es  {aux_2[indice]}")
	toc = time.perf_counter()
	tiempo_2 = toc-tic
	print(f"EL tiempo de ejecucion de la funcion con threads fue de  { tiempo_2}")
	#se puede usar estos print para confirmar el orden en el que llegaron las cantidades , de cada thread
	#print(aux)
	#print(aux_2)
	if tiempo_2<tiempo_1:
		print("EL tiempo de ejecucion del programa con threads es menor, entonces la funcion implementada con threads es más rapida")
	else:
		print("EL tiempo de ejecucion del programa sin threads es menor, entonces la funcion implementada sin threads es más rapida")





	
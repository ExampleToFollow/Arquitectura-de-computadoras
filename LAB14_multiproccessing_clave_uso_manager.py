import time
from werkzeug.security import check_password_hash
from multiprocessing import Pool, Manager

"""
Esta es la contraseña que usted tiene que adivinar. Está encriptada para que no pueda saber cuál es la respuesta correcta a priori.
Lo que tiene que hacer es generar combinaciones de 3 letras y llamar a la función comparar_con_password_correcto(línea 24 de la plantilla)
"""
contrasena_correcta = 'pbkdf2:sha256:260000$rTY0haIFRzP8wDDk$57d9f180198cecb45120b772c1317b561f390d677f3f76e36e0d02ac269ad224'


# Arreglo con las letras del abecedario. Puede serle de ayuda, no es obligatorio que lo use
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

"""
Función que sirve para comparar su palabra(cadena de 3 caracteres) con la contraseña correcta.
Entrada: Su cadena de 3 caracteres
Salida: True(verdadero) si es que coincide con la contraseña correcta, caso contrario retorna False(falso)
"""
def comparar_con_password_correcto(palabra):
	return check_password_hash(contrasena_correcta, palabra)

vocales = ['a','e' , 'i', 'o', 'u']

def fuerza_bruta_serial(abecedario):
	password = ""
	for i in vocales:
		for j in vocales:
			for h in abecedario:
				password = i+j+h
				#print(password)
				if (comparar_con_password_correcto(password)):
					print(f"La contraseña es {password}")
					return password
				
def fuerza_bruta_paralelo( vocal , abecedario, aux):
		for j in vocales:
			for h in abecedario:
				if (not aux.value):
					password = vocal+j+h
					#print(password)
					if (comparar_con_password_correcto(password)):
						print(f"La contraseña es {password}")
						aux.value = True
						return password
				else:
					return
				
if __name__ == "__main__":
	print("Ejecucion de la funcion serial:")
	tic=time.perf_counter()
	fuerza_bruta_serial(abecedario)
	toc = time.perf_counter()
	time_serial = toc-tic
	print(f"Tiempo de ejecucion de la funcion serial es { time_serial}")
	print("Ejecucion de la funcion en paralelo:")
	tic = time.perf_counter()
	manager=Manager()
	aux = manager.Value('b',False)
	p= Pool(processes =5)
	args= [(i,abecedario,aux) for i in vocales]
	p.starmap(fuerza_bruta_paralelo, args)
	p.close()
	p.join()
	toc = time.perf_counter()
	time_paralelo= toc-tic
	print(f"El tiempo de ejecucion de la funcion en paralelo es de { time_paralelo}")

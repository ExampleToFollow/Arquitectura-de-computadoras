import random
import socket

my_IP= "127.0.0.1"
port = 5000
#diccionario de donde se escoge
dictionary = ["hola", "pucp" , "ciclo", "arquitectura", " ingenieria ", " servidor", "computadora", "amazon", "peru" , "universidad" , "jazz"]
def reemplazar_caracteres(word, hidden_word, client_guess):
    for idx in range(0, len(word)):
        if word[idx] == client_guess:
            hidden_word = hidden_word[:idx] + client_guess + hidden_word[idx+1:] 
    return hidden_word

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    sock.bind((my_IP, port))
    print(f"Arrancando servidor en { my_IP}:{ port} ")
    sock.listen(1)
    try:
        while True:
            print("Esperando una nueva conexion de un cliente")
            sock.settimeout(1)
            while True:
                try:
                    conn , addr = sock.accept()
                    break
                except TimeoutError:
                    pass
            sock.settimeout(None)
            print(f"...conexión de  : ( {my_IP } , {port} )")
            word = random.choice(dictionary)
            hidden_word = "*"*len(word)
            contador = 0
            while True : 
                word_recv = conn.recv(1024)
                if word_recv.decode() == 'start':
                    print("Recibi comando estart ")
                    print(f"Palabra elegida : {word}")
                    conn.sendall(hidden_word.encode())
                elif word_recv.decode() == 'stop':
                    print("Desconectando del clente, Terminamos el juego")
                    break
                else:
                    print(f"Client guess : { word_recv.decode()}")
                    new_hidden_word = reemplazar_caracteres(word, hidden_word , word_recv.decode())
                    if new_hidden_word == hidden_word :
                        conn.sendall (b'Intento incorrecto')
                        contador +=1
                        if contador == 5:
                            break
                    else:
                        conn.sendall(new_hidden_word.encode())
                        hidden_word = new_hidden_word
                        if new_hidden_word == word:
                            print("El cliente adivino la palabra")
                            break
            conn.close()
            print("Cerrando conexión con el cliente")
    except KeyboardInterrupt:
        print("Cerrando servidor")
        sock.close()





import random
import socket
my_IP = "127.0.0.1"
port = 5027
#Diccionario de donde se escoge palabras al azar para el juego
dictionary = ["hola", "pucp", "ciclo", "arquitectura", "ingenieria", "servidor", "computadora", "amazon", "peru", "universidad", "jazz"]
def ahorcado(intento):
    if(intento==1):
        print("______________________________\n|                           _|_\n|                           |__|\n|                            | \n|                              ")


    elif(intento==2):
        print("______________________________\n|                           _|_\n|                           |__|\n|                           _| \n|                              ")


    elif(intento==3):
        print("______________________________\n|                           _|_\n|                           |__|\n|                           _|_\n|                              ")


    elif(intento==4):
        print("______________________________\n|                           _|_\n|                           |__|\n|                           _|_\n|                             \\")

    elif(intento==5):
        print("______________________________\n|                           _|_\n|                           |__|\n|                           _|_\n|                            /\\")


def adivinando(word, hidden_word, client_guess):
    for idx in range(0, len(word)):
        if word[idx] == client_guess:
            hidden_word = hidden_word[:idx] + client_guess + hidden_word[idx+1:] 
    return hidden_word
SOCKET_BUFFER =1024
  
if __name__ == "__main__":
    
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server_address = (my_IP ,port)
    sock.bind(server_address)
    
    print(f"arrancando el servidor en {server_address[0]} : { server_address[1]}")
    sock.listen(1)
    
    print("Esperando la conexion de un cliente")
    connection, client_address = sock.accept()
    
    print(f"...conexion de ({client_address[0]} , {client_address[1]})")
    
    #elegimos las palabra random
    secret_word = random.choice(dictionary)
    
    hidden_word = ""

    for i in range(len(secret_word)):
        hidden_word = hidden_word + "*"
    
    hidden_word_para_enviar = hidden_word.encode()
    intento = 0
    try:
        while True:
            msg = connection.recv(SOCKET_BUFFER)
            msg = msg.decode()
            if msg == 'start':
                print("Recibi comando start")
                print(f"Palabra elegida : {secret_word}")
                connection.sendall(hidden_word_para_enviar)
            else:
                try:
                    if (msg == "stop"):
                        print("EL juego acabo")
                        break
                    print(f"Client guess : {msg}")
                    #Vamos generando una nueva palabra de referencia con lo quevaya adivinando el cliente
                    reference = adivinando(secret_word, hidden_word, msg)
                    if reference == hidden_word:
                        connection.sendall(b'Intento incorrecto')
                        
                        intento = intento +1 
                        #esto es un extra xd
                        print("se equivoco")
                        ahorcado(intento)
                        if intento ==5:
                            print("Se le acabaron los intentos")
                            break
                    else:
                        reference_para_enviar=reference.encode()
                        connection.sendall(reference_para_enviar)
                        hidden_word = reference
                        if hidden_word == secret_word:
                            print("Felicidades, adivinaste la palabra")
                            break
                except BrokenPipeError:
                    connection.close()
        connection.close()
    except KeyboardInterrupt:
        sock.close()
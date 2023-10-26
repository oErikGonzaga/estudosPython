from socket import *

server = "localhost"
port = 43210

# AF_INET, Tipo de Identificação: Ex. ip ou hostname
# SOCK_DGRAM, Utilizada para socket UDP (utilizado para broadcast)

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((server, port))
msg = ""

while msg != "x":
    msg = input("Sua mensagem: ")

    if msg.upper() == "X":  # Verifica se a mensagem é "X" (maiúsculo)
        break  # Encerra o loop se a mensagem for "X"

    obj_socket.sendto(msg.encode(), (server, port))
    dados, origem = obj_socket.recvfrom(65535)
    print("Resposta do Servidor: ", dados.decode())

obj_socket.close()

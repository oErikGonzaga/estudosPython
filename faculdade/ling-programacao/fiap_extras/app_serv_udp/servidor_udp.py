from socket import *

server = "localhost"
port = 43210

# AF_INET, Tipo de Identificação: Ex. ip ou hostname
# SOCK_DGRAM, Utilizada para socket UDP (utilizado para broadcast)

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((server, port))
print("Servidor pronto....")


while True:
    dados, origem = obj_socket.recvfrom(65535)
    print("Origem..............: ", origem)
    print("Dados recebidos: ", dados.decode())
    response = input("Digite a resposta: ")
    obj_socket.sendto(response.encode(), origem)


obj_socket.close()

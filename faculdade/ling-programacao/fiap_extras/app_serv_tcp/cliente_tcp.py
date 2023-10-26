# Importa a classe socket da biblioteca socket.
from socket import *

# Define o endereço do servidor como 'localhost' e a porta como 8081.
server = "localhost"
port = 8081

# Solicita ao usuário que digite uma mensagem.
# Codifica a mensagem para bytes usando 'utf-8'.
msg = bytes(input("Digite: "), 'utf-8')

# Cria um objeto de socket utilizando a família de endereços AF_INET para IPv4 e o tipo de socket SOCK_STREAM para TCP.
obj_socket = socket(AF_INET, SOCK_STREAM)

# Conecta-se ao servidor utilizando o método connect, passando o endereço do servidor e a porta.
obj_socket.connect((server, port))

# Envia a mensagem codificada para o servidor usando o método send.
obj_socket.send(msg)

# Aguarda a resposta do servidor com no máximo 1024 bytes usando o método recv.
response = obj_socket.recv(1024)

# Imprime a resposta recebida do servidor.
print("Recebemos: ", response)

# Fecha a conexão com o servidor usando o método close.
obj_socket.close()




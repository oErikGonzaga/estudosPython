# Importa a classe socket da biblioteca socket.
from socket import *

# Define o endereço do servidor como 'localhost' e a porta como 8081.
server = "localhost"
port = 8081

# Cria um objeto de socket utilizando a família de endereços AF_INET para IPv4 e o tipo de socket SOCK_STREAM para TCP.
obj_socket = socket(AF_INET, SOCK_STREAM)

# Liga o socket ao endereço do servidor e à porta especificada usando o método bind.
obj_socket.bind((server, port))

# Coloca o socket em modo de escuta (listen) para aceitar conexões usando o método listen.
obj_socket.listen(2)

print("Waiting for a customer...")


# Entra em um loop infinito para aceitar conexões de clientes.
while True:

    # Quando uma conexão é aceita, obtém um objeto de conexão (con) e o endereço do cliente.
    con, client = obj_socket.accept()
    print("Conectado ao: ", client)

    # Entra em outro loop para lidar com a comunicação com o cliente.
    while True:

        # Recebe mensagens do cliente usando o método recv.
        received_msg = str(con.recv(1024))

        # Imprime a mensagem recebida.
        print("Recebemos: ", received_msg)

        # Envia uma mensagem de boas-vindas ao cliente usando o método send.
        send_msg = b'Ola Cliente, seja bem vindo'

        con.send(send_msg)
        break

    # Fecha a conexão com o cliente usando o método close.
    con.close()




# Importa a classe FTP da biblioteca ftplib.
from ftplib import *

# Conecta-se ao servidor FTP em 'ftp.ibiblio.org'.
ftp = FTP('ftp.ibiblio.org')

# Imprime a mensagem de boas-vindas do servidor FTP.
print(ftp.getwelcome())

# Solicita ao usuário que digite o nome de usuário (o usuario é vazio)
# e senha (o senha é vazia) para autenticação no servidor FTP.
user = input("Digite o usuario: ")
password = input("Digite a Senha: ")

# Realiza a autenticação no servidor FTP usando o nome de usuário e senha fornecidos.
ftp.login(user, password)

# Imprime o diretório atual de trabalho (diretório inicial) no servidor FTP.
print("Diretório atual de trabalho: ", ftp.pwd())

# Altera o diretório atual de trabalho para 'pub'.
ftp.cwd('pub')

# Imprime o diretório atual de trabalho após a alteração.
print("Diretorio Corrente: ", ftp.pwd())

# Lista os arquivos e diretórios no diretório atual usando o comando LIST.
print(ftp.retrlines('LIST'))

# Encerra a conexão FTP com o servidor.
ftp.quit()



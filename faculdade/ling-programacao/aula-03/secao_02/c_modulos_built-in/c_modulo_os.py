# OS é um módulo built-in usado para executar comandos no sistema operacional
import os

os.getcwd()  # retorna uma string com o caminho do diretório de trabalho.

os.listdir()  # Retorna uma lista com todas as entradas de um diretório. Se não for especificado um caminho,
# então a busca é realizada em outro diretório de trabalho.

os.cpu_count()  # retorna um inteiro com o número de CPUs do sistema.
os.getlogin()  # retorna o nome do usuário logado.
os.getenv(key='path')  # retorna uma string com o conteúdo de uma variável de ambiente especificada na key.
os.getpid()  # retorna o id do processo atual.

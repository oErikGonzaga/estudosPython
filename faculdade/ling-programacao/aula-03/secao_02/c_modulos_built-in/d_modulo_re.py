# O módulo re (regular expression) fornece funções para busca de padrões em um texto.
from re import search, match, split

string = 'meuArquivo_20-01-2020.py'
padrao = "[a-zA-Z]*"

# Varre a string procurando o primeiro local onde o padrão de expressão regular produz uma correspondência e o retorna.
# Retorna None se nenhuma correspondência é achada.
txt1 = search(padrao, string).group()

# Procura por um padrão no começo da string. Retorna None se a sequência não corresponder ao padrão.
txt2 = match(padrao, string).group()

# Divide uma string pelas ocorrências do padrão.
txt3 = split("_", string)[0]

print(txt1)
print(txt2)
print(txt3)

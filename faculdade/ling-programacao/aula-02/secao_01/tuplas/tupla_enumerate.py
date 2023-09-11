# Para cada item de um enumerate(), é impressa uma tupla

vogais = ('a', 'e', 'i', 'o', 'u')

for item in enumerate(vogais):
    print(item)

# Construtor tuple() para transformar o resultado em uma tupla,
# No qual temos uma tupla de tuplas. No segundo comentário,
print(tuple(enumerate(vogais)))

# Usando o contrutor list(), no qual temos uma lista de tuplas.
print(list(enumerate(vogais)))

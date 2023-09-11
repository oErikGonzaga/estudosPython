# Criando uma lista vazia e adicionando valores
vogais = []

# append() adiciona um novo valor ao final da lista
vogais.append('a')
vogais.append('e')
vogais.append('i')
vogais.append('o')
vogais.append('u')

# enumerate(), é usada para percorrer um objeto iterável retornando a posição e o valor
for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")

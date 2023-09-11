frutas = ["maça", "banana", "uva", "mamão", "maça"]
notas = [8.7, 5.2, 10, 3.5]

# min - Verifica se o item existe na lista
print("maça" in frutas)
print("abacate" in frutas)

# min - Verifica se o item não existe na lista
print("abacate" not in frutas)

# min - busca o menor valor na lista
print(min(frutas))

# max - busca o maior valor na lista
print(max(notas))

# Verifica a quantidade do item passado no paramentro.
print(frutas.count("maça"))

# Junta as listas
print(frutas + notas)

# multiplica a lista ao final dela
print(2 * frutas)

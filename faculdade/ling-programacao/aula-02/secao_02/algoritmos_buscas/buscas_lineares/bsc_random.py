import random


# Verificando uma lista de números criados aleatóriamente.

def busca_linear(lst, valor):
    for elemento in lst:
        if valor == elemento:
            return True
    return False


lista = random.sample(range(1000), 50)
print(sorted(lista))

print(busca_linear(lista, 5))

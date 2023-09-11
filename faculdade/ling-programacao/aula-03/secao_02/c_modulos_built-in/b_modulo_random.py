#  Random é um módulo built-in usado para criar número aleatórios
from random import randint, choice, sample

print(randint(0, 100))  # retorna um valor inteiro aleatório, de modo que esse número esteja entre a, b.

print(choice([1, 10, -1, 100]))  # extrai um valor de forma aleatória de uma certa sequência.

print(sample(range(100000), k=12))  # retorna uma lista com k elementos, extraídos da população.

# Funções Built-In (type, range e eval)

a = 2
b = 1

equacao = input("Digite a fórmula geral da equação linear (a * x + b): ")
print(f"\nA entrada do usuário {equacao} é do {type(equacao)}")

for x in range(5):
    y = eval(equacao)
    print(f"\nResultado da equação para x = {x} é {y}")

# A função eval() basicamente recebe uma string contendo código Python
# válido e retorna o resultado da avaliação desse código.

# A função range() gera números inteiros em uma sequência,
# começando de um valor inicial (inclusive) até um valor final (exclusivo),
# com um incremento especificado (opcional).
# (Sintaxe: range(inicio, fim, incremento))


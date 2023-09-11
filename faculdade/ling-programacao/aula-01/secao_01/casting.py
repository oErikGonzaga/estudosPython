# Exemplo de erro de Casting

a = 2
b = 0.5
c = 1
x = input("Digite o valor de x: ")

y = a * x ** 2 + b * x + c
print(f"O resultado de y para x = {x} é {y}.")


# Correção do Erro

a = 2
b = 0.5
c = 1
x = input("Digite o valor de x: ")

x = float(x)
# aqui fazemos a conversão da string para o tipo numérico

y = a * x ** 2 + b * x + c
print(f"O resultado de y para x = {x} é {y}.")
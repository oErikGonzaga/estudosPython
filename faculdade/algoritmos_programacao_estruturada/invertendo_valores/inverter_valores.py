print("Acertar valores")

qtd_homens = input(print("Digite a quantidade de Mulheres: "))
qtd_mulheres = input(print("Digite a quantidade de Homens: "))

troca = qtd_mulheres
qtd_mulheres = qtd_homens
qtd_homens = troca

print(f"A quantidade correta de mulheres é: {qtd_mulheres}")
print(f"A quantidade correta de homens é: {qtd_homens}")

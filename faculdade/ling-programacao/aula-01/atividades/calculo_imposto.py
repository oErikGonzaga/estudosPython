# Salario do Colaborador

salario = float(input("Colaborador, insira o valor do seu salário: "))

isento = 1903.98
base_7 = 2826.65
base_15 = 3751.05
base_22 = 4664.68

deducao = float(0)

if salario > base_22:
    deducao = (salario / 100) * 27.5
    print(f"O colaborador deve pagar R$ {round(deducao, 2)} de Imposto")
elif base_15 < salario <= base_22:
    deducao = (salario / 100) * 22.5
    print(f"O colaborador deve pagar R$ {round(deducao, 2)} de Imposto")
elif base_7 < salario <= base_15:
    deducao = (salario / 100) * 15
    print(f"O colaborador deve pagar R$ {round(deducao, 2)} de Imposto")
elif isento < salario <= base_7:
    deducao = (salario / 100) * 7.5
    print(f"O colaborador deve pagar R$ {round(deducao, 2)} de Imposto")
else:
    print("O colaborador é isento de imposto")



# Resposta do Exercicio:

# salario = 0
# salario = float(input("Digite o salário do colaborador: "))
#
# if salario <= 1903.98:
#     print(f"O colaborador isento de imposto.")
#     print(f"Salário a receber = {salario}")
# elif salario <= 2826.65:
#     print(f"O colaborador deve pagar R$ 142,80 de imposto.")
#     print(f"Salário a receber = {salario - 142.80}")
# elif salario <= 3751.05:
#     print(f"O colaborador deve pagar R$ 354,80 de imposto.")
#     print(f"Salário a receber = {salario - 354.80}")
# elif salario <= 4664.68:
#     print(f"O colaborador deve pagar R$ 636,13 de imposto.")
#     print(f"Salário a receber = {salario - 636.13}")
# else:
#     print(f"O colaborador deve pagar R$ 869,36 de imposto.")
#     print(f"Salário a receber = {salario - 869.36}")

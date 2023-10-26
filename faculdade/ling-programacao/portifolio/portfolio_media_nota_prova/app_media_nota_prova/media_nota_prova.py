from funcoes.solicitar_notas import solicitar_nota

# Declarar as variáveis
np1 = solicitar_nota("Digite a nota da Prova 1: ")
np2 = solicitar_nota("Digite a nota da Prova 2: ")

# Calcular a média
media = (np1 + np2) / 2

# Exibir a média final
print("Média Final:", media)

# Verificar se o aluno foi aprovado ou reprovado
if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado.")

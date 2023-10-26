from app_media_nota_prova.funcoes.solicitar_notas import solicitar_nota

# Declarar as variáveis
nota_prova1 = solicitar_nota("Digite a nota da Prova 1: ")
nota_prova2 = solicitar_nota("Digite a nota da Prova 2: ")

# Calcular a média
media = (nota_prova1 + nota_prova2) / 2

# Exibir a média final
print("Média Final:", media)

# Verificar se o aluno foi aprovado ou reprovado
if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado.")

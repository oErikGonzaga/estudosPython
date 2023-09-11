# Estrutura Lógica - and

qtd_faltas = int(input("Digite a quantidade de faltas: "))
media_final = float(input("Digite a média final: "))

if qtd_faltas <= 5 and media_final >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno Reprovado!")

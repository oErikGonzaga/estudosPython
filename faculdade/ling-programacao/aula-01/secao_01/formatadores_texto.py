# Capturando através da função input()
# Armazenando na str nome

# A função input() contém a string "Digite um nome:",
# mas captura o valor que será inserido no "terminal".
# Por último armazena dentro da variável nome.

nome = input("Digite um nome: ")
print()

# Modo 1 - usando formatadores de caracteres (igual na linguagem C) para imprimir variável e texto
# (%s) Insere o valor apresentando ao final do código, respeitando a ordem de inserção.
print("Primeiro Exemplo")
print("Olá %s, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world.\n" % (nome))

# Modo 2 - usando a função format() para imprimir variável e texto
# formata o texto acrescentando o valor nome dentro das chaves {}.
print("Segundo Exemplo")
print("Olá {}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world.\n".format(nome))

# Modo 2 - usando a função format() para imprimir variável e texto
# formata o texto acrescentando o valor nome dentro das chaves {}.
print("Terceiro Exemplo")
print("Olá {}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world.".format(nome))
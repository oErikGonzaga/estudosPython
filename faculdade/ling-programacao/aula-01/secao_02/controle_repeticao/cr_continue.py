# Estrutura de Repetição - continue

disciplina = "Linguagem de Programação"

txt = ""

# txt = []

for c in disciplina:
    if c == ' ':
        continue
    else:
        print(c)
        txt += c
        # txt += c.split (criando uma lista)

print(txt)

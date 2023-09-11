texto = ("Neste sentido, a consolidação das estruturas representa uma abertura para a melhoria dos níveis de "
         "motivação departamental.")


# len - Imprime o tamanho do texto
print(f"Tamanho do texto: {len(texto)} caracteres")

# in - busca na lista o valor especificado e retorna True
print(f"\"estruturas\" no texto: {'estruturas' in texto}")

# count - informa quantos itens especificados existem na lista
print(f"Quantidade de ç no texto: {texto.count('ç')}")

# Exibe somente os valores especificados da posição inicial a posição final -1
print(f"As 5 primeiras letras no texto são: {texto[0:6]}")

# upper - Deixa todos os caracteres em maiuscula
print(texto.upper())

# upper - Deixa todos os caracteres em minuscula
print(texto.lower())

# replace - Substitue um caracter por outro (incluindo espaços)
print(texto.replace(" ", "_"))

print(f"Texto = {texto}")

print(f"Tamanho do texto = {len(texto)}\n")
texto = texto.replace(",", "").replace(".", "")
print(texto)

palavras = texto.split()
print(f"Palavras = {palavras}")
print(f"Tamanho de Palavras = {len(palavras)}")

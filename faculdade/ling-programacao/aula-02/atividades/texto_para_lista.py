texto = """Operadores de String Python oferece operadores para processar texto (ou seja, valores de string). Assim 
como os números, as strings podem ser comparadas usando operadores de comparação: ==, !=, <, > e assim por diante. O 
operador ==, por exemplo, retorna True se as strings nos dois lados do operador tiverem o mesmo valor (Perkovic, 
p. 23, 2016)."""

print(f"Tamanho do texto: {len(texto)}")
texto = texto.lower()
texto = texto.replace(",", "").replace(".", "").replace("(", "").replace(")", "").replace("\n", " ")

lista_palavras = texto.split()
print(f"Tamanho da lista de palavras: {len(lista_palavras)}")

total_palavra = lista_palavras.count("string") + lista_palavras.count("strings")
print(f"Quantidade de vezes que a palavra string ou string aparecem: {total_palavra}")

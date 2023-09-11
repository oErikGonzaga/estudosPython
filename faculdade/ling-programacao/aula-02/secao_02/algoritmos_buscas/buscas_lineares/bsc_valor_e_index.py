# Buscando valor e o index.

def procurar_valor(lista, valor):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        if valor == lista[i]:
            return i
    return None


vogais = "aeiou"

result = procurar_valor(lista=vogais, valor='x')

if result is not None:
    print(f'Valor encontrado na posição {result}')
else:
    print('Valor não encontrado')

def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:

        # Encontra o elemento que divide a lista ao meio
        meio = (minimo + maximo) // 2

        # Verifica se o valor procurado está a esquerda ou direita do valor central
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:

            # Se o valor for encontrado para aqui
            return True

    # Se chegar até aqui, significa que o valor não foi encontrado
    return False


lista = list(range(1, 50))

print(lista)
print('\n', executar_busca_binaria(lista=lista, valor=10))
print('\n', executar_busca_binaria(lista=lista, valor=200))

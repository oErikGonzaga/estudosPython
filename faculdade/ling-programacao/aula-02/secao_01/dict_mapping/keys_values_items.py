cadastro = {
    'nome': ['João', 'Ana', 'Pedro', 'Marcela'],
    'cidade': ['São Paulo', 'São Paulo', 'Rio de Janeiro', 'Curitiba'],
    'idade': [25, 33, 37, 18]
}

print("len(cadastro) = ", len(cadastro))

# cadastro.keys(): retorna uma lista com todas as chaves no dicionário.
print("\n cadastro.keys() = \n", cadastro.keys())

# cadastro.values(): retorna uma lista com os valores. Como os valores também são listas, temos uma lista de listas.
print("\n cadastro.values() = \n", cadastro.values())

# cadastro.items(): retorna uma lista de tuplas, cada uma das quais é composta pela chave e pelo valor.
print("\n cadastro.items() = \n", cadastro.items())

print("\n cadastro['nome'] = ", cadastro['nome'])
print("\n cadastro['nome'][2] = ", cadastro['nome'][2])
print("\n cadastro['idade'][2:] = ", cadastro['idade'][2:])

# Total de elementos somando quantos há em cada chave

print(len(cadastro['nome']))
print(len(cadastro['cidade']))
print(len(cadastro['idade']))

# somando items com listcomp
qtde_itens = sum([len(cadastro[chave]) for chave in cadastro])

# Um objeto do tipo set habilita operações matemáticas de conjuntos,
# tais como: união, intersecção, diferenteça, etc


# sem uso do construtor
vogais_1 = {'aeiou'}
print(type(vogais_1), vogais_1)

# construtor com string
vogais_2 = set('aeiouaaaaaa')
print(type(vogais_2), vogais_2)

# construtor com lista
vogais_3 = set(['a', 'e', 'i', 'o', 'u'])
print(type(vogais_3), vogais_3)

# construtor com tupla
vogais_4 = set(('a', 'e', 'i', 'o', 'u'))
print(type(vogais_4), vogais_4)

print(set('banana'))

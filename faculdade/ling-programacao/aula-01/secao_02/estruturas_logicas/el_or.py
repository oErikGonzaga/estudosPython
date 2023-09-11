# Estrutura Lógica - or

a = 15
b = 9
c = 9

result1 = (b == c or a < b and a < c)

# Precedência Booleana
result2 = ((b == c or a < b) and a < c)

print(result1)
print(result2)

import numpy

m1 = numpy.zeros((3, 3))  # Cria matriz 3 x 3 somente com zero
m2 = numpy.ones((2, 2))  # Cria matriz 2 x 2 somente com um
m3 = numpy.eye(4)  # Cria matriz 4 x 4 identidade
m4 = numpy.random.randint(low=0, high=100, size=10).reshape(2, 5)  # Cria matriz 2 X 5 com números inteiros

print('\n numpy.zeros((3, 3)) = \n', numpy.zeros((3, 3)))
print('\n numpy.ones((2,2)) = \n', numpy.ones((2, 2)))
print('\n numpy.eye(4) = \n', numpy.eye(4))
print('\n m4 = \n', m4)

print(f"\nSoma dos valores em m4 = {m4.sum()}")
print(f"Valor mínimo em m4 = {m4.min()}")
print(f"Valor máximo em m4 = {m4.max()}")
print(f"Média dos valores em m4 = {m4.mean()}")

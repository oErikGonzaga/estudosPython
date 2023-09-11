# A classe-filho não herdará o construtor dos pais. O construtor da classe-filho
# sobrescreve (override) o da classe-pai. Para utilizar o construtor da classe-base,
# é necessário invocá-lo explicitamente,

class Int42(int):
    def __init__(self, n):
        int.__init__(n)

    def __add__(a, b):
        return 42

    def __str__(n):
        return '42'


a = Int42(7)
b = Int42(13)

print(a + b)
print(a)
print(b)

c = int(7)
d = int(13)

print(c + d)
print(c)
print(d)

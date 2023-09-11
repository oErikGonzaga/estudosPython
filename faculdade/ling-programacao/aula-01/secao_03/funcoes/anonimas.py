# função anônima é uma função que não é construída com o "def"

(lambda x: x + 1)(x=3)

# ou

(lambda x, y: x + y)(x=3, y=2)

# ou

somar = lambda x, y: x + y
somar(x=5, y=3)

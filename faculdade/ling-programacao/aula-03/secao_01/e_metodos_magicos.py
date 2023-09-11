# Uma classe herda, mesmo que não declarado explicitamente,
# todos os recursos de uma classe-base chamada object.

class Pessoa:
    def __init__(self):
        self.cpf = None
        self.nome = None
        self.endereco = None


print(dir(Pessoa))

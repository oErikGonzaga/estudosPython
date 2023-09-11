# Um atributo de instância é uma variável precedida com o parâmetro self,
# ou seja, a sintaxe para criar e utilizar é self.nome_atributo.

class Televisao:

    # é possível determinar um estado inicial para variáveis de instâncias por meio do método construtor da classe.
    def __init__(self):
        self.volume = 10

    def aumentar_volume(self):
        self.volume = self.volume + 1

    def diminuir_volume(self):
        self.volume -= 1


tv = Televisao()

print(f"Volume ao ligar a TV: {tv.volume}")

tv.aumentar_volume()
print(f"Volume atual: {tv.volume}")

tv.diminuir_volume()
tv.diminuir_volume()
print(f"Volume atual: {tv.volume}")

from datetime import datetime


# A reutilização de código por meio da herança, permite
# que uma classe-filha herde os recursos da classe-pai.

class Pessoa:
    def __init__(self):
        self.cpf = None
        self.nome = None
        self.endereco = None


class Funcionario(Pessoa):
    def __init__(self):
        super().__init__()
        self.matricula = None
        self.salario = None
        self.registro_ponto = []

    def bater_ponto(self, entrada_saida):
        self.registro_ponto.append((entrada_saida, datetime.now()))
        pass

    def mostrar_registro(self):
        for registro in self.registro_ponto:
            print(f"{registro[0]}: {registro[1]}")


class Cliente(Pessoa):
    def __init__(self):
        super().__init__()
        self.codigo = None
        self.data_cadastro = None


f1 = Funcionario()

f1.nome = "João das Couves"
f1.cpf = "123.456.678-90"
f1.endereco = {'Logradouro': 'Rua Aburá', 'Numero': 150, 'CEP': 0o2541000, 'Cidade': 'São Paulo', 'Estado': 'SP'}

print(f1.nome)
print(f1.cpf)
endereco = f1.endereco

for chave, valor in endereco.items():
    print(f"\t{chave}: {valor}")

f1.bater_ponto("\nEntrada")
f1.bater_ponto("Saída para almoço")
f1.bater_ponto("Retorno do almoço")
f1.bater_ponto("Saída")

f1.mostrar_registro()

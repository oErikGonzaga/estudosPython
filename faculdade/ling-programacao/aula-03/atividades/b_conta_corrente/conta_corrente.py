class ContaCorrente:
    def __init__(self, nome):
        self.nome = nome
        self.email = None
        self.telefone = None
        self.saldo = float(0)

    def saldo(self):
        return self.saldo

    def depositar(self, valor):
        self.saldo += valor

    def _checar_saldo(self):
        return self.saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            print("Não há saldo suficiente!")
            return False


class ContaPF(ContaCorrente):
    def __init__(self, nome, cpf):
        ContaCorrente.__init__(self, nome)
        self.cpf = cpf

    def solicitar_emprestimo(self, valor):
        return self.saldo >= 500


class ContaPJ(ContaCorrente):
    def __init__(self, nome, cnpj):
        ContaCorrente.__init__(self, nome)
        self.cnpj = cnpj

    def sacar_emprestimo(self, valor):
        return valor <= 5000

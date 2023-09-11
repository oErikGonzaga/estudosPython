# um atributo é privado, ele só pode ser acessado por membros da própria classe.
# Declararando um atributo privado, precisamos de métodos que acessem e recuperam os valores ali guardados.

class ContaCorrente:

    def __init__(self):
        self._saldo = 0

    @property  # marcação como getter
    def saldo(self):
        return self._saldo

    @saldo.setter
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
        else:
            "Saldo insuficiente"


cc = ContaCorrente()

print(cc.saldo)

cc.depositar = 100
print(cc.saldo)

cc.sacar(50)
print(cc.saldo)

class Calculadora:

    def somar(self, n1, n2):
        return n1 + n2

    def subtrair(self, n1, n2):
        return n1 - n2

    def multiplicar(self, n1, n2):
        return n1 * n2

    def dividir(self, n1, n2):
        return n1 / n2

    def resto_divisao(self, n1, n2):
        return n1 % n2

    def porcentagem(self, percent, valor):
        return (percent * valor) / 100


calc = Calculadora()

print('Soma:', calc.somar(4, 3))
print('Subtração:', calc.subtrair(13, 7))
print('Multiplicação:', calc.multiplicar(2, 4))
print('Divisão:', calc.dividir(16, 5))
print('Resto da divisão:', calc.resto_divisao(7, 3))
print('Porcentagem:', calc.porcentagem(7, 2500))

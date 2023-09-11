def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        return "Divisão por zero não é permitida."
    return a / b


def main():
    print("Calculadora Simples")
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação desejada: ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = soma(num1, num2)
    elif escolha == '2':
        resultado = subtracao(num1, num2)
    elif escolha == '3':
        resultado = multiplicacao(num1, num2)
    elif escolha == '4':
        resultado = divisao(num1, num2)
    else:
        resultado = "Opção inválida."

    print("Resultado:", resultado)


if __name__ == "__main__":
    main()

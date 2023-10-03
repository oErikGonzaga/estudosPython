from funcoes.calcular_imc import *
from funcoes.diagnosticar_imc import *

while True:
    try:
        # Entrada de peso e altura
        peso = input("Informe seu peso em Kg: ").replace(',', '.')
        peso = float(peso)

        altura = input("Informe sua altura em Mts: ").replace(',', '.')
        altura = float(altura)

        # Cálculo do IMC e diagnóstico
        resultado = calcular_imc(peso, altura)
        mensagem = diagnosticar_imc(resultado)

        # Exibição do resultado
        print("\nSeu IMC é:", resultado)
        print("Info:", mensagem)

        # Sai do loop quando a entrada é válida
        break

    except ValueError:
        print("Insira somente números.\nTente novamente.")

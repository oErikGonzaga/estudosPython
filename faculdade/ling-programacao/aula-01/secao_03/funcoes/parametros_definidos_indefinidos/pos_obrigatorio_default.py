# Parâmetro posicional, obrigatório, com valor default (padrão).

def calcular_desconto(valor, desconto=0.0):
    (valor_com_desconto) = (valor - (valor * desconto))
    return valor_com_desconto


valor1 = calcular_desconto(100)
valor2 = calcular_desconto(100, 0.25)

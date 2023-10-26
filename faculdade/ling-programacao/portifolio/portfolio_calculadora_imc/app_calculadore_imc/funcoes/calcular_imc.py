def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) com base no peso e altura fornecidos.

    Parâmetros:
        peso (float): Peso em quilogramas.
        altura (float): Altura em metros.

    Retorna:
        float: O Índice de Massa Corporal (IMC).
    """

    if peso <= 0:
        print("Peso inválido. O peso deve ser maior que zero.")
        return None

    if altura <= 0:
        print("Altura inválida. A altura deve ser maior que zero.")
        return None

    imc = peso / (altura * altura)  # Calcula o IMC
    return round(imc, 2)  # Retorna o IMC arredondado para 2 casas decimais

def diagnosticar_imc(resultado):
    """
    Retorna uma mensagem de diagnóstico com base no resultado do IMC.

    Parâmetros:
        resultado (float): O Índice de Massa Corporal (IMC) calculado.

    Retorna:
        str: Uma mensagem de diagnóstico baseada no IMC.
    """

    # Definição das faixas de IMC e suas mensagens correspondentes
    faixas_imc = [
        (float('-inf'), 16.9, 'Muito abaixo do peso'),
        (17, 18.4, 'Abaixo do peso'),
        (18.5, 24.9, 'Peso normal'),
        (25, 29.9, 'Acima do peso'),
        (30, 34.9, 'Obesidade Grau I'),
        (35, 40, 'Obesidade Grau II'),
        (40, float('inf'), 'Obesidade Grau III')
    ]

    for faixa in faixas_imc:
        if faixa[0] <= resultado <= faixa[1]:
            return faixa[2]

    return 'IMC fora das faixas conhecidas'

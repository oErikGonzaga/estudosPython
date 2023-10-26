def solicitar_nota(mensagem):
    while True:
        try:
            entrada = input(mensagem)
            nota = float(entrada.replace(',', '.'))

            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Insira somente números.\nTente novamente.")
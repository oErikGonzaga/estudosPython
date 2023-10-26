def solicitar_nota(nota_prova):
    while True:
        try:
            entrada = input(nota_prova)
            nota = float(entrada.replace(',', '.'))

            if not 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. A nota deve estar entre 0 e 10.")

            # Utilzando operador de negaçào para obter o mesmo resultado:
            # if not (nota_prova1 > -1 and nota_prova1 < 11):
            # print("Nota inválida. A nota deve estar entre 0 e 10.")

        except ValueError:
            print("Insira somente números.\nTente novamente.")

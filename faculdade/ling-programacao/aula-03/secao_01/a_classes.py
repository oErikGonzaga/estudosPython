class PrimeiraClasse:
    @staticmethod
    def imprimir_mensagem(nome):  # Criando um método
        print(f'Olá {nome}, seja bem vindo!')


objeto1 = PrimeiraClasse()  # Instanciando um objeto do tipo PrimeiraClasse
objeto1.imprimir_mensagem('João')  # invocando o método

print("Cadastro de Dados do Aluno")

nome = str(input("Digite o nome completo do aluno: "))
endereco = str(input(f"Digite o endereço do aluno {nome}: "))
numero = int(input(f"Digite o numero da residência: {endereco} "))
complemento = str(input("Digite o complemento da residência: "))
cep = str(input(f"Digite o CEP do endereço: {endereco} {numero} {complemento} - "))
estado = str(input("Digite o Estado: "))
cidade = str(input(f"Digite o Cidade do Estado de {estado}: "))

cadastro = (f"\nCadastro do Aluno: \n"
            f"\nNome: {nome};\n"
            f"Endereço: {endereco}, {numero}, {complemento};\n"
            f"CEP: {cep};\n"
            f"Cidade: {cidade};\n"
            f"Estado: {estado};\n"
            f"\nAluno cadastrado com sucesso.")

print(cadastro)

import sqlite3

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

cursor.execute('''
INSERT INTO fornecedor  (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa A', '11.111.111/0001-11', 'São Paulo', 'SP', '01010-010', 2020-01-01)
''')

cursor.execute('''
INSERT INTO fornecedor  (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa B', '22.222.222/2222-22', 'Belo Horizonte', 'MG', '02020-020', 2019-02-02)''')

cursor.execute("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa C', '33.333.333/3333-33', 'Curitiba', 'PR', '03030-030', '2020-01-01')
""")

conn.commit()
print("Dados inseridos!")
print("Descrição do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)
cursor.close()
conn.close()

import sqlite3

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

dados = [
    ('Empresa D', '44.444.444/4444-44', 'São Paulo', 'SP', '44444-444', '2020-01-01'),
    ('Empresa E', '55.555.555/5555-55', 'São Paulo', 'SP', '55555-555', '2020-01-01'),
    ('Empresa F', '66.666.666/6666-66', 'São Paulo', 'SP', '66666-666', '2020-01-01')
]

cursor.executemany('''
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES (?, ?, ?, ?, ?, ?)''', dados)

conn.commit()
print("Dados inseridos!")
print("Descrição do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)
cursor.close()
conn.close()

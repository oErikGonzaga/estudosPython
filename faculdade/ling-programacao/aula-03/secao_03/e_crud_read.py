import sqlite3

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM fornecedor")
resultado = cursor.fetchall()

print("Descrição do cursor: ", cursor.description)
print("Linhas afetadas: ", cursor.rowcount)

for linha in resultado:
    print(linha)


print(f'\nResultado: {resultado[:2]}')

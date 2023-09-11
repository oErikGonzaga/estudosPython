import sqlite3

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM fornecedor WHERE id_fornecedor = 4')
resultado1 = cursor.fetchall()

cursor.execute('SELECT * FROM fornecedor WHERE estado = \'MG\'')
resultado2 = cursor.fetchall()

print(resultado1)
print(resultado2)

cursor.close()
conn.close()

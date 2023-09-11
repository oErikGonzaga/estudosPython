import sqlite3

conn = sqlite3.connect('aulaDB.db')

ddl_drop = '''
DROP TABLE fornecedor;
'''


cursor = conn.cursor()
cursor.execute(ddl_drop)
print(type(cursor))

print('Tabela excluída!')
print("Linhas afetadas: ", cursor.rowcount)
cursor.close()
conn.close()

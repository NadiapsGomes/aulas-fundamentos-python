#Crie uma base de dados chamada loja.db - passo 1
# e uma tabela chamada produtos com as seguintes colunas: #passo2
# id (INTEGER, PRIMARY KEY, autoincrement),
#nome (TEXT), preco (REAL), stock (INTEGER).

import sqlite3 #passo1

conn = sqlite3.connect('loja.db') #passo1

cursor = conn.cursor() #passo2
cursor.execute('''
        CREATE TABLE IF NOT EXISTS loja (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
conn.commit()
conn.close()


#Insira 10 produtos fictícios na tabela criada anteriormente.
# Cada produto deve ter um nome, preço e quantidade de stock.
# Dica: Pode utilizar o executemany()

import sqlite3

conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS loja (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        stock INTEGER NOT NULL
    )
''')

produtos = [
    ("Base", 23.99, 10),
    ("Rimel", 12.30, 7),
    ("Sombra nude", 17.99, 4),
    ("Sombra vibrante", 23.49, 2),
    ("Sombra shine", 14.90, 3),
    ("Epic eyeliner", 14.99, 2),
    ("Lápis de sobrancelha", 4.99, 3),
    ("Conjunto pincéis", 32.40, 1),
    ("Lipstick Brown", 12.99, 3),
    ("Lipstick femme fatale", 22.90, 3)
]

cursor.executemany("INSERT INTO loja (nome, preco, stock) VALUES (?, ?, ?)", produtos)

conn.commit()
conn.close()


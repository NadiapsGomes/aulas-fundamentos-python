#Altere os preços dos produtos com os ids 5, 6 e 7.

import sqlite3

conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

novos_precos = {
    5: 16.50,
    6: 15.75,
    7: 5.49
}

for id_produto, preco in novos_precos.items():
    cursor.execute("UPDATE loja SET preco = ? WHERE id = ?", (preco, id_produto))

conn.commit()
conn.close()
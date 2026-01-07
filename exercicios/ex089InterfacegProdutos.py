#Crie uma Interface Simples no Terminal para Gestão de Produtos.
# O programa deve permitir:
# Adicionar novos produtos (com nome, preço e stock),
# Mostrar todos os produtos da base de dados,
# Alterar um produto existente (nome, preço ou stock).

import sqlite3
conn = sqlite3.connect('gProdutos.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS gProdutos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        stock INTEGER NOT NULL
    )
''')
conn.commit()


def adicionar_produto():
    nome = input("Produto: ")
    preco = float(input("Preço: "))
    stock = int(input("Stock: "))
    cursor.execute("INSERT INTO gProdutos (nome, preco, stock) VALUES (?, ?, ?)", (nome, preco, stock))
    conn.commit()
    print("Adicionado com sucesso!\n")


def mostrar_produtos():
    cursor.execute("SELECT * FROM gProdutos")
    produtos = cursor.fetchall()
    if produtos:
        print("\n***Lista de Produtos***")
        for produto in produtos:
            print(f"ID: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]:.2f}, Stock: {produto[3]}")
        print()
    else:
        print("Sem resultados.\n")


def alterar_produto():
    id_produto = int(input("Digite o ID do produto que deseja alterar: "))
    cursor.execute("SELECT * FROM gProdutos WHERE id = ?", (id_produto,))
    produto = cursor.fetchone()

    if produto:
        print(f"Produto selecionado: {produto[1]}, Preço: {produto[2]:.2f}, Stock: {produto[3]}")
        novo_nome = input("Novo nome (pressione Enter para manter): ")
        novo_preco = input("Novo preço (pressione Enter para manter): ")
        novo_stock = input("Novo stock (pressione Enter para manter): ")

        if novo_nome == "":
            novo_nome = produto[1]
        if novo_preco == "":
            novo_preco = produto[2]
        else:
            novo_preco = float(novo_preco)
        if novo_stock == "":
            novo_stock = produto[3]
        else:
            novo_stock = int(novo_stock)

        cursor.execute("UPDATE gProdutos SET nome = ?, preco = ?, stock = ? WHERE id = ?",
                       (novo_nome, novo_preco, novo_stock, id_produto))
        conn.commit()
        print("Produto atualizado com sucesso!\n")
    else:
        print("Produto não encontrado.\n")


while True:
    print("***GESTOR DE PRODUTOS***")
    print("[1] - Adicionar produto")
    print("[2] - Mostrar produtos")
    print("[3] - Alterar produto")
    print("[4] - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        mostrar_produtos()
    elif opcao == "3":
        alterar_produto()
    elif opcao == "4":
        print("A sair...")
        break
    else:
        print("Opção inválida!\n")

conn.close()
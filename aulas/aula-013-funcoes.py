#Estabelecer a ligação
#1 - Importar a biblioteca necessária

import sqlite3

def cabecalho(txt:str)->None:
    print(f'{txt}')

#2 - Iniciar a conexão
def conectar():
    try:
        return sqlite3.connect('tarefas.db')
    except Exception as e:
        print(f'Erro ao iniciar ligação à base de dados: {str(e)}')
        return ''


#Criar uma tabela
def criar_tabela():
    #criar conexao
    conn = conectar()

    #criar o cursor
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            descricao TEXT NOT NULL, 
            estado TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_tarefa():
    cabecalho('ADICIONAR TAREFA')
    descricao_tarefa = input('Descrição: ').strip()
    estado_tarefa = 'Pendente'

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tarefas (descricao, estado) VALUES (?, ?),",
    (descricao_tarefa, estado_tarefa))
    conn.commit()
    conn.close()
    print(f'Tarefa "{descricao_tarefa}" adicionada com sucesso')

def ver_tarefa():
    cabecalho('MOSTRAR TAREFAS')
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()

    for tarefa in tarefas:
        print('-----------------------------------------------------------')
        print(f'{tarefa[0]} | DESCRICAO: {tarefa[1]} | ESTADO: {tarefa[2]}')

def terminar_tarefa():
    pass

def apagar_tarefa():
    pass


criar_tabela()

def menu():
    criar_tabela()
    while True:
        print('[1] - Adicionar tarefa')
        print('[2] - Ver tarefa')
        print('[3] - Concluir tarefa')
        print('[4] - Apagar tarefa')
        print('[5] - Sair')
        opcao = int(input('-->'))

        match opcao:
            case 1:
                adicionar_tarefa()
            case 2:
                ver_tarefa()
            case 3:
                terminar_tarefa()
            case 4:
                apagar_tarefa()
            case 5:
                break
            case _:
                print('Opção inválida...')

if __name__=='__main__':
    menu()
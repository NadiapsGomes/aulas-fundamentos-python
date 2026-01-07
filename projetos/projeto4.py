#Desenvolva um programa em python, de acordo com todas as boas práticas aprendidas,
# que simule um bloco de notas. O programa deve permitir:
#1. Adicionar notas a um ficheiro .txt;
#2. Mostrar todas as notas gravadas;
#3. Apagar todas as notas;
#4. Pesquisar notas por palavra-chave.

# Inês / Julia / Nádia

from pathlib import Path
import os

pasta = Path('../bloco_notas')
ficheiro = pasta / 'notas.txt'
os.makedirs(pasta, exist_ok=True)

def adicionar_nota():

    nota = input('Nota:\n--> ')

    with ficheiro.open('a', encoding='utf-8', errors='ignore') as file:
        file.write(nota + '\n')

    print('Nota adicionada!\n')


def mostrar_notas():

    if ficheiro.exists():
        notas = ficheiro.read_text(encoding='utf-8').strip()
    else:
        notas = ''

    print('\n--- Nota Gravadas ---')
    print(notas if notas else '\nNenhuma nota encontrada.')


def apagar_notas():

    ficheiro.write_text('', encoding='utf-8', errors='ignore')
    print('\nNotas apagadas!\n')


def pesquisar_notas():

    palavra = input('Palavra-chave:\n--> ').lower()
    resultados = []

    with ficheiro.open('r', encoding='utf-8', errors='ignore') as aberto:
        for numero, linha in enumerate(aberto):
            if palavra in linha.lower():
                resultados.append((numero, linha.strip()))

    print('\n--- Pesquisa ---\n')

    if resultados:

        for numero, x in resultados:
            print(x)

    else:
        print(f'\nNenhuma nota encontrada com a palavra {palavra}!')


def mostrar_menu():
    print('\n--- BLOCO DE NOTAS ---\n')
    print('[ 1 ] - Adicionar nota')
    print('[ 2 ] - Mostrar todas as notas')
    print('[ 3 ] - Apagar todas as notas')
    print('[ 4 ] - Pesquisar notas por palavra-chave')
    print('[ 5 ] - Sair\n')

def main(): #aqui podemos usar a função "match opcao: case 1: x, case 2: "
    while True:
        mostrar_menu()
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            adicionar_nota()
        elif opcao == '2':
            mostrar_notas()
        elif opcao == '3':
            apagar_notas()
        elif opcao == '4':
            pesquisar_notas()
        elif opcao == '5':
            print('A sair do programa...')
            break
        else:
            print('\nOpção inválida! Tente novamente!\n')

if __name__ == '__main__':
    main()
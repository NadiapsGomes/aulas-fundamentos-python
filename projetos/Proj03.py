#Nádia, Telmo, Júlia

print('***CRIADOR DE FORMAS***')
opcao = 0

while opcao != 5:
    print('Selecione uma das seguintes opções')
    print('[1] Pirâmide alinhada à esquerda')
    print('[2] Pirâmide alinhada à direita')
    print('[3] Pirâmide centralizada')
    print('[4] Desenhar X')
    print('[5] Sair')
    opcao = int(input('Escolha uma das opções: '))

    if opcao == 1:
        for c in range(0, 6):
            print('*' * (c+1))

    elif opcao == 2:
        for c in range(0, 6):
            espacos = ' ' * (5 - c)
            print(espacos + '*' * (c+1))

    elif opcao == 3:
        altura = 5
        for c in range(0, 5):
            espacos = altura - c - 1
            asteriscos = 2 * c + 1
            print(' ' * espacos + '*' * asteriscos)

    elif opcao == 4:
        num_linhas = 5
        for c in range(0,5):
            for x in range(0,5):
                if c == x or c + x == num_linhas - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
    else:
        print('Saiu')


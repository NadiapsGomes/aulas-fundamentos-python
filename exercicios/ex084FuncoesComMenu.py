#Desenvolva um programa que simule uma calculadora interativa com diferentes funcionalidades.
# O programa deve exibir um menu com várias opções
# e permitir que o utilizador escolha uma das opções.
# O programa deve executar a funcionalidade escolhida e
# quando terminar deve voltar a apresentar o menu.
# Use o tratamento de exceções para lidar com entradas inválidas (como strings ou caracteres)
# e erros matemáticos (como divisão por zero).
# Todas as funções devem estar num módulo bem estruturado e documentado.
#Função- Calculadora [SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO]
#Função- Tabuada
#Função- Par ou Ímpar
#Função- Números primos
#Função- Factorial

from time import sleep


def cabecalho(txt):
    print('-' * 30)
    print(f'{txt:^30}')
    print('-' * 30)


def calculadora():
    cabecalho('Calculadora')
    try:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
    except ValueError:
        print('Erro: Digite apenas números válidos.')
        return

    print(f'Soma: {num1} + {num2} = {num1 + num2}')
    print(f'Subtração: {num1} - {num2} = {num1 - num2}')
    print(f'Multiplicação: {num1} x {num2} = {num1 * num2}')
    if num2 == 0:
        print('Divisão: erro (divisão por zero).')
    else:
        print(f'Divisão: {num1} / {num2} = {num1 / num2}')


def tabuada():
    cabecalho('Tabuada')
    try:
        num = int(input('Digite um número inteiro de 1 a 10: '))
    except ValueError:
        print('Erro: Digite um número inteiro.')
        return

    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')


def par_ou_impar():
    cabecalho('Par ou Ímpar')
    try:
        numero = int(input('Digite um número inteiro: '))
    except ValueError:
        print('Erro: Digite um número inteiro.')
        return

    if numero % 2 == 0:
        print(f'O número {numero} é PAR.')
    else:
        print(f'O número {numero} é ÍMPAR.')


def primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    c = 3
    while c * c <= n:
        if n % c == 0:
            return False
        c += 2
    return True


def primos():
    cabecalho('Números Primos')
    try:
        numero = int(input('Digite um número inteiro: '))
    except ValueError:
        print('Erro: Digite um número inteiro.')
        return

    if primo(numero):
        print(f'O número {numero} É PRIMO.')
    else:
        print(f'O número {numero} NÃO É PRIMO.')


def fatorial():
    cabecalho('Fatorial')
    try:
        numero = int(input('Digite um número inteiro não negativo: '))
    except ValueError:
        print('Erro: Digite um número inteiro.')
        return

    if numero < 0:
        print('Erro: não existe fatorial de número negativo.')
        return

    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i

    print(f'{numero}! = {resultado}')


def menu():
    print()
    cabecalho('MENU')
    print('[1] Calculadora')
    print('[2] Tabuada')
    print('[3] Par ou Ímpar')
    print('[4] Números Primos')
    print('[5] Fatorial')
    print('[6] Sair')
    print()


def main():
    while True:
        try:
            menu()
            opcao = input('Escolha uma opção (1-6): ').strip()
            if opcao == '1':
                calculadora()
            elif opcao == '2':
                tabuada()
            elif opcao == '3':
                par_ou_impar()
            elif opcao == '4':
                primos()
            elif opcao == '5':
                fatorial()
            elif opcao == '6':
                print('A sair...')
                sleep(0.8)
                break
            else:
                print('Opção inválida. Escolha um número entre 1 e 6.')

            print()
            input('Prima Enter para voltar ao menu...')
        except ():
            print('\nSaída interrompida pelo utilizador. A sair.')
            break

if __name__ == '__main__':
    main()
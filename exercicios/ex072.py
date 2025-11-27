#Crie um programa que tenha uma função que receba 3 parâmetros:
# inicio, fim e passo.
# O programa deve realizar 3 contagens através da função.
#a) De 1 até 20, de 2 em 2
#b) De 10 até 0, de 1 em 1
#c) Contagem personalizada

def contagem(inicio: int, fim: int, passo: int):

    if passo < 1:
        p=1
        print('Passo vai iniciar no valor padrão.')

    if inicio > fim:
        passo = -passo
        fim = fim -1

    for c in range(inicio, fim, passo):
        print(c)

contagem(1,20,2)
contagem(10,0,1)

print('Contagem personalizada')
inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))

print(contagem(inicio, fim, passo))


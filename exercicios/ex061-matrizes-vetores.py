# Crie um programa que crie uma matriz 3x3
# Preencha com valores lidos pelo teclado
# No final mostre a matriz vom a formatação adequada

#[[], [], []] - matriz (lista dentro de lista)
numeros = list()

[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for linha in range (0,3):
    temporario = list()

    for coluna in range(0,3): #estou a pedir 3 x um númrero
        num = int(input('Digite um número: '))
        temporario.append(num)

    numeros.append(temporario[:])

print(numeros)

#[1, 2, 3] - isto é um vetor - indice zero da lista
#[4, 5, 6] - isto é outro vetor - indice um da lista
#[7, 8, 9] - terceiro vetor - indice dois da lista
#que conjuntamente compõem uma matriz

print(numeros[0][2]) #imprime o indice dois da lista no indice zero - linha, coluna

for lista in numeros:
    print(lista)

for lista in numeros:
    for valor in lista:
        print(valor, end=' ')
    print()
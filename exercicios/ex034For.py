#Faça um programa que leia 10 números e conte quantos deles são pares.

quantidade_pares = 0
for c in range (0, 10):
    numero = int(input(f'Digite um número '))

    if numero %2==0:
        quantidade_pares+=1
        print(f'Digitou {quantidade_pares} números pares')


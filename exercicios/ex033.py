#Faça um programa que leia 5 números inteiros e mostre a soma desses números.

soma = 0

for c in range (0, 5):
    numero=int(input(f'Insira um algarismo '))
    #soma = soma + numero
    soma += numero

print('O resultado totaliza', soma)

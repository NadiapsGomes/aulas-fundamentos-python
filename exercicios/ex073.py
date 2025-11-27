#Crie um programa que tenha uma função que receba vários parâmetros
# como valores inteiros.
# O programa deve analisar todos os valores e dizer qual deles é o maior.

def maior(*valor): #*permite colocar as variaveis que eu quiser dentro de maior
    maior = max(valor)
    print(f'O maior valor é {maior}')

maior(5,6,200,4899, 7463)
maior(1,2,3,4)

#Desenvolva um programa que leia um número qualquer e que mostre o seu fatorial.
#Na matemática, o fatorial de um número natural n, denotado por n!,
# é o produto de todos os naturais menores ou iguais a n.
# O fatorial de n também é igual ao produto de n e o fatorial de seu antecessor:
# Por exemplo, O valor de 0! é 1, conforme a convenção para um produto vazio.


numero = int(input('Digite um número: '))

if numero == 0 or numero == 1:
    print(f'O fatorial de {numero} é 1.')
else:
    fatorial = 1

    while numero >= 1:
        if numero == 1:
            print(numero, end=' = ')
        else:
            print(numero, end=' x ')
        fatorial *= numero
        numero -= 1

    print(fatorial)
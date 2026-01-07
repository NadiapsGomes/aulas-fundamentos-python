#Crie um programa que leia vários números inteiros e que termine apenas
# quando o utilizador digitar a opção para parar.
# No final mostre quantos números o utilizador inseriu e qual a soma entre eles.

contador = 0
soma = 0

while True:
    numero = int(input("Digite um número inteiro: "))

    if numero == 0:
        break

    soma += numero
    contador += 1

print("\n--- Resultado ---")
print(f"Quantidade de números inseridos: {contador}")
print(f"Soma total: {soma}")

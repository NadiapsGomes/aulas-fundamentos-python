#Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas;
#✓ O nome com todas as letras minúsculas;
# Quantidade de letras sem espaços;
#Quantas letras tem o primeiro nome.

nome = input('Digite o seu nome: ').strip()

print(nome.upper())

print(nome.lower())

qtd_espacos = nome.count(' ')# Quantidade de letras sem espaços;
print(len(nome) - qtd_espacos)

pEspaco = nome.find(' ')# Quantas letras tem o primeiro nome.
print(len(nome[:5]))






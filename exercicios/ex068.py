#Crie um programa que leia o nome, sexo e idade de várias pessoas,
# guardando cada dado num dicionário e todos os dicionários numa lista.
# No final mostre:
#a) Quantas pessoas foram registadas;
#b) Qual a média de idades do grupo;
#c) Quantas mulheres foram registadas;
#d) Quantos homens com idade acima da média foram registados.

obj_estudo = []
pessoa = dict()

pessoa['Nome: '] = input('Digite o seu nome: ')
pessoa['Idade: '] = int(input('Digite o seu ano de nascimento: '))
pessoa['Sexo: '] = float(input('Digite o valor dos seus rendimentos: '))

obj_estudo.append(pessoa)

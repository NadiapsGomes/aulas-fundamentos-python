#Crie um programa que leia o nome, sexo e idade de várias pessoas,
# guardando cada dado num dicionário e todos os dicionários numa lista.
# No final mostre:
#a) Quantas pessoas foram registadas;
#b) Qual a média de idades do grupo;
#c) Quantas mulheres foram registadas;
#d) Quantos homens com idade acima da média foram registados.

pessoas = []
dados = dict()
qtd_pessoas = 0
soma_idades = 0
qtd_mulheres = 0

while True:
    dados = dict()
    dados['nome'] = input('Digite um nome: ').strip()
    while True:
        dados['sexo'] = input('Digite o sexo [m/f]: ').strip().lower()
        if dados ['sexo'] != 'm' and dados ['sexo'] != 'f':
            print('Por favor introduza um sexo válido.')
        else:
            break



    dados['idade'] = int(input('Digite a idade: '))

    soma_idades += dados['idade']
    pessoas.append(dados.copy())
    dados.clear()
    qtd_pessoas += 1

    opcao = input('Digite sim para terminar')
    if opcao == 'sim':
        break





#Crie um programa que guarde o aproveitamento de um jogador de futebol.
# O programa deverá ler o nome, quantos jogos jogou
# e a quantidade de golos por jogo e guardar tudo num dicionário.
# No dicionário, deve calcular a média de golos por jogo.

aproveitamento = []
jogador = dict()

jogador['Nome: '] = input('Digite o nome do jogador: ')
jogador['Número de jogos da temporada'] = int(input('Digite o número de jogos em que participou: '))
jogador['Quantidade de golos'] = int(input('Quantos golos marcou? '))

jogador['Média'] = jogador['Quantidade de golos'] / jogador['Número de jogos da temporada']
print(jogador)


#Crie um programa que sorteie a ordem de jogada num jogo
# ao “atirar um dado ao ar”.
# Cada jogador terá um número aleatório associado dentro de um dicionário.
# No final ordene o ranking para ver a ordem de jogada.

from time import sleep
from random import choice

participantes = []
qtd_jogadores = 0
jogador = dict()
print('Quantidade jogadores: ')
while qtd_jogadores < 4:

    jogador['jogador'] = input('Digite um participante: ')

    participantes.append(jogador.copy())
    qtd_jogadores += 1
sleep(1)
print(f'Participantes no jogo: {participantes}')

ordem_jogada = choice(participantes)
sleep(1)
print(f'Ordem de jogo: {ordem_jogada["jogador"]}')



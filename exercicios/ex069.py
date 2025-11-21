# Melhore o exercício 67 para que permita a entrada de vários jogadores.
# Defina um sistema de visualização que permita ao utilizar
# procurar pelos resultados de um jogador específico.

from random import randint
jogadores = ''

nomes = ['Ricardo', 'Luanna', 'Pedro', 'Viktor', 'Inês', 'Nádia']

for c in range(len(nomes)):
    jogador = dict()

    jogador['Nome'] = nomes[c]
    jogador['Quantidade de golos'] = randint(1,20)
    jogador['Quantidade de jogos'] = randint(1,10)
    jogador['Média de golos'] = jogador['Quantidade de golos'] / jogador['Quantidade de jogos']


    jogadores.append(jogador.copy)

print(jogadores)
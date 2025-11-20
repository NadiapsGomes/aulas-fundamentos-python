from time import sleep
from random import randint

#palpites para o euromilhoes,
#perguntar quantas chaves serão geradas
#deve sortear aleatoriamente 5 num de 1 a 50 [sem repetir] e duas estrelas de 1 a 12 [sem repetir]
#cada sorteio deve ser guardado numa lista

import random

numapostas = int(input("Quantas chaves deseja gerar? "))
sleep(1)

chaves = []

for apostas in range(0, numapostas):
    numeros = []
    while len(numeros) < 5:
        n = random.randint(1, 50)
        if n not in numeros:
            numeros.append(n)

    estrelas = []
    while len(estrelas) < 2:
        e = random.randint(1, 12)
        if e not in estrelas:
            estrelas.append(e)

    numeros.sort()
    estrelas.sort()

    chaves.append([numeros, estrelas])

for c, chave in enumerate(chaves, 1):
    print(f"Chave {c}: Números {chave[0]} | Estrelas {chave[1]}")
#Crie um programa com um tuple com os 20 primeiros classificados
# do Campeonato Espanhol de Futebol.
# Depois mostre: a) Os primeiros 5 classificados.
# b) Os últimos 4 classificados.
#c) Uma lista com as equipas por ordem alfabética.
#d) A posição da equipa Las Palmas.

from time import sleep

print('***APURAMENTO CAMPEONATO DA LIGA DE FUTEBOL ESPANHOL***')
sleep(1)

equipas = 'Real Madrid', 'Barcelona', 'Villarreal', 'Real Betis','Atlético de Madrid', 'Sevilla', 'Elche', 'Athletic Club', 'Espanyol','Alavés', 'Getafe', 'Osasuna', 'Levante', 'Rayo Vallecano', 'Valencia','Celta de Vigo', 'Real Oviedo', 'Girona', 'Real Sociedad', 'Mallorca'

for c in range(0, len(equipas)):
    print(f'{c+1} -> {equipas[c]}')
    sleep(0.5)

print('5 Primeiros Classificados:')
for indice, equipa in enumerate(equipas):
    if indice == 5:
        break
    else:
        print(f'\t{indice+1}º - {equipa}')
print('---------------------------------------')

print('4 Últimos Classificados:')
TAM = len(equipas)
for indice, equipa in enumerate(equipas):
    if indice >= TAM - 4:
        print(f'\t{indice+1}º - {equipa}')
    else:
        continue
print('---------------------------------------')

print('Equipas por ordem alfabética:')
for equipa in sorted(equipas):
    print('\t', equipa)
print('---------------------------------------')

print('Posição da equipa Las Palmas:')
esta_la = False
indice_las_palmas = ''

for indice, equipa in enumerate(equipas):
    if equipa == 'Las Palmas':
        esta_la = True
        indice_las_palmas = indice

if esta_la:
    print(f'Las Palmas -> {indice_las_palmas + 1}º lugar')
else:
    print('Las Palmas não está classificado.')

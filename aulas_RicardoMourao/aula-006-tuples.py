estante = input('Digite uma consola '), input('Digite outra consola ')
print(estante)

nomes = 'Nadia', 'Julia', 'Telmo', 'Victor', 'Rafael', 'Daniel'

nome = 'Ricardo'

#variavel composta que pode ter mais que um valor
#acedo isoladamente através dos indices print(nomes[])
#len é o todo - o tamanho da minha variável.

tam = len(nomes)
for c in range(0, len(nomes)):
    print(f'{c} -> {nomes(c)}')

for nome in nomes:
    print(nome)

for indice, nome in enumerate(nomes): #isola o valor e o indice desse valor
    print(f'No indice {indice} o valor é {nome})

# estante = input('Digite uma consola: '), input('Digite outra consola')


...
nomes = ('Nádia', 'Julia', 'Alexandra', 'Telmo',
         'Victor', 'Rafael', 'Daniel', 'Leticia',
         'Roman', 'Pedro', 'Francisca', 'Inês', 32, True, 3.14)

for c in range(0, len(nomes)):
    print(f'{c} -> {nomes[c]}')

for nome in nomes:
    print(nome)

for indice, nome in enumerate(nomes):
    print(f'No índice {indice} o valor é {nome}')

print(type(nomes))

# estante = input('Digite uma consola: '), input('Digite outra consola')

nomes = ('Nádia', 'Julia', 'Alexandra', 'Telmo',
         'Victor', 'Rafael', 'Daniel', 'Leticia',
         'Roman', 'Pedro', 'Francisca', 'Inês', 32, True, 3.14)

for c in range(0, len(nomes)):
    print(f'{c} -> {nomes[c]}')

for nome in nomes:
    print(nome)

for indice, nome in enumerate(nomes):
    print(f'No índice {indice} o valor é {nome}')

print(type(nomes))
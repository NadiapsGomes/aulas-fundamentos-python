#Desafio 40 Guanabara
notas = []

print('Insira as suas notas e digite "0" quando terminar.')

while True:
    nota = float(input('Digite as suas notas: '))

    if nota == 0:
        break
    notas.append(nota)

media = sum(notas)/len(notas)

print(f'As notas inseridas foram {notas}. A sua média é {media}')

if 0 < media < 5:
    print('REPROVADO')
elif 5 < media < 9:
    print('EM RECUPERAÇÃO')
else:
    print('APROVADO')

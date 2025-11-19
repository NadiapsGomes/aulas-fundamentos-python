#Crie um programa que leia 5 notas de um aluno e calcule a sua média.
# >=9.5 passou
# >8 e < 9.5 em recuperação
# <8 reprova

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))
nota4 = float(input('Digite a 4ª nota: '))
nota5 = float(input('Digite a 5ª nota: '))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print('A média obtida foi de:',media)

if media >= 9.5:
    print('Aprovado')
elif media > 8:
    print('Em recuperação')
else:
    print('Reprovado')


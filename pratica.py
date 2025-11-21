#rie um programa que leia um número inteiro qualquer
# mostre na tela a sua unidade, dezena, centena e milhar.

num = int(input('Digite um número: '))
print(num)

n = str(num)

print(f'Unidade:{n[3]}')
print(f'Dezena:{n[2]}')
print(f'Centena:{n[1]}')
print(f'Milhar:{n[0]}')
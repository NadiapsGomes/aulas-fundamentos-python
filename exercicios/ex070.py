#Crie um programa que tenha uma função chamada area()
# que receba as dimensões de um terreno e mostre a área do terreno.

def area(l:float, c:float):
    area=l*c
    print(f'A área do terreno é {area:.2f}m2')

largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))

area(largura, comprimento)
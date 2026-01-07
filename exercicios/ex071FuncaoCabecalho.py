#Crie um programa que tenha uma função que receba um texto como parâmetro
# e que mostre uma mensagem com tamanho adaptável.

def cabecalho(txt:str):
    tamanho = len(txt) + 3

    print(f'-='*int(tamanho / 2))
    print(f'{txt:^{tamanho}}')
    print(f'-='*int(tamanho / 2))

cabecalho('Amanhã é Blackfriday.')
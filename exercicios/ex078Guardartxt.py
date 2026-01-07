#Crie um programa com uma função chamada fatorial(), que receba
# dois parâmetros: o primeiro será o número a calcular o fatorial
# e o segundo será opcional e lógico que indique se será exibido
# ou não o processo de cálculo do fatorial.
# O fatorial deve ser guardado num ficheiro txt.


def fatorial (numero: int, mostra=False)-> str:

    from math import factorial
    fatorial_calculado = factorial(numero)

    if mostra: #if mostra == True ou if not mostra: if mostra == False
        while numero >1:
            if numero ==1:
                print(numero, end=' = ')
            else:
                print(numero, end=' x ')
            numero -= 1
        print(fatorial_calculado)

        return 'fans'


def guarda_txt(txt:str) -> None:
    from pathlib import Path

    caminho= Path(r'fatorial.txt')

    with caminho.open(mode='a',encoding='utf-8',errors='ignore') as file:
        file.write(f'-{txt}\n')

    print('Fatorial criado com sucesso.')

    #criar variável que represente o caminho
    #criar variável que represente o ficheiro aberto



fatorial(8, True)



#Crie um programa que tenha uma função que vai receber como parâmetro
# o ano de nascimento de uma pessoa e que crie um ficheiro que informe
# se a pessoa já pode tirar a carta de condução,
# se precisa de autorização do encarregado de educação
#ou se não pode.
#+18 anos – pode
#-16 anos – não pode
#-18 e +16 – com autorização

from pathlib import Path
from datetime import date

def requisitos(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if idade < 16:
        resultado = "Ainda não está elegível para tirar a carta de condução."
    elif 16 <= idade < 18:
        resultado = "Pode tirar a carta de condução apenas com autorização do encarregado de educação."
    else:
        resultado = "Pode inscrever-se para tirar a carta de condução."

    with open("../requisitos/requisitos", "w") as ficheiro:
        ficheiro.write(f"Ano de nascimento: {ano_nascimento}\n")
        ficheiro.write(f"Idade: {idade}\n")
        ficheiro.write(f"Resultado: {resultado}\n")

    print(" Ficheiro 'requisitos.txt' criado com sucesso!")

try:
    ano = int(input("Digite o seu ano de nascimento: "))
    requisitos(ano)

except ValueError:
    print("Erro: Digite um ano válido.")

#Crie um programa que leia o nome e a média de um aluno,
#calculando a sua situação, tudo dentro de um dicionário.
#No final mostre todo o conteúdo do dicionário.
#Situação: Média >= 9,5 – Aprovado, Média < 9,5 - Reprovado

turma = []
qtd_alunos = 3
aluno = dict() #ou {}

for c in range(qtd_alunos):
    aluno['Nome'] = input('Digite um nome: ')
    aluno['Média'] = float(input(f'Digite a média do(a) {aluno["Nome"]}: '))

    aluno['Situação'] = 'Aprovado' if aluno['Média']>=9.5 else 'Reprovado'

    turma.append(aluno.copy())

print(turma)
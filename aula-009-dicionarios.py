#listas = [Nádia, 20, aprovada]
#print(listas[0])

turma = []
qtd_alunos = 5
aluno = dict() #ou {}

for c in range(qtd_alunos):
    aluno['Nome'] = input('Digite um nome: ')
    aluno['Média'] = float(input(f'Digite a média do(a) {aluno["Nome"]}: '))

    aluno['Situação'] = 'Aprovado' if aluno['Média']>=9.5 else 'Reprovado'

    turma.append(aluno.copy())

print(turma)
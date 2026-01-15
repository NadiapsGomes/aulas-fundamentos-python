valor = float(input('Qual o valor da moradia que pretende adquirir? '))
print(f'O valor a financiar será de {valor} €')

rendimento = float(input('Qual é o rendimento do seu agregado familiar? '))
print(f'Para um empréstimo de {valor}, consideramos {rendimento}€ de ativos.')

nrAnos = int(input('Em quantos anos tenciona liquidar esse empréstimo?'))

taxaEsforco = rendimento*30/100
print(taxaEsforco)

nrMeses = nrAnos*12
print(nrMeses)

prestacao = valor/nrMeses
print(prestacao)


if prestacao >= taxaEsforco:
    print('O seu empréstimo não pode ser concedido porque a prestação excede 30% dos rendimentos do agregado.')
else:
    print(f'EMPRÉSTIMO CONCEDIDO! O valor da sua prestação mensal será {prestacao}€')
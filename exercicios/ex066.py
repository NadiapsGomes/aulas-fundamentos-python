#Crie um simulador de crédito habitação simples e sem taxas,
# que solicite o nome, ano de nascimento, rendimentos mensais,
#despesas mensais, montante do crédito e prazo em anos,
# guardando tudo dentro de um dicionário.
# Calcule, acrescentando ao dicionário, a idade, o remanescente após despesas,
# quanto deverá pagar mensalmente pelo crédito e se o crédito foi aprovado
# sempre que o remanescente seja superior ao valor mensal do crédito.
from datetime import date
from time import sleep
sleep(1)
print('------------------------------')
print('SIMULADOR DE CRÉDITO HABITAÇÃO')
print('------------------------------')

elementos = []
contraente = dict()
ano_atual = date.today().year


contraente['Nome: '] = input('Digite o seu nome: ')
contraente['Ano de nascimento: '] = int(input('Digite o seu ano de nascimento: '))
contraente['Rendimentos mensais: '] = float(input('Digite o valor dos seus rendimentos: '))
contraente['Despesas mensais: '] = float(input('Digite o valor mensal das suas despesas: '))
contraente['Valor do crédito: '] = int(input('Qual o valor que necessita para o seu crédito '))
contraente['Número de anos para pagamento: '] = int(input('Em quantos anos pretende liquidar o seu crédito: '))


contraente['Idade'] = ano_atual-contraente['Ano de nascimento: ']
contraente['Remanescente'] = contraente['Rendimentos mensais: ']- contraente['Despesas mensais: ']
contraente['Crédito'] = contraente['Valor do crédito: '] / (contraente['Número de anos para pagamento: '] *12)

if contraente['Remanescente'] > contraente['Crédito']:
    print(f'Crédito aprovado!')

else:
    print('NEGADO, vai trabalhar mais')


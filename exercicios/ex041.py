#Desenvolva um programa que faça 3 perguntas ao utilizador
# e apenas aceite como resposta “V” ou “F”.
# Caso esteja errado, peça para repetir a resposta até ter um valor correto.

resposta = ''
print('A hipotenusa ao quadrado resulta da soma dos catetos ao quadrado? ')
while resposta != 'V' and resposta != 'F':
    resposta = input('[V / F]: ').strip().upper()
    if resposta == 'V':
        print('Boa! Acertas-te.')
    elif resposta == 'F':
        print('Vai estudar o teorema de pitágoras!')
    else:
        print('Inválido. Responde V/F')

resposta = ''
print('O mês de Dezembro, à exceção do Natal, tem mais dois feriados? ')
while resposta != 'V' and resposta != 'F':
    resposta = input('[V / F]: ').strip().upper()
    if resposta == 'V':
        print('Elaia!')
    elif resposta == 'F':
        print('Tem sim. Verifica o calendário')
    else:
        print('Resposta inválida.')

print('9x9 = 81?')
while True:
    resposta = input('[V / F]: ').strip().upper()
    if resposta == 'V':
        print('Sete macacos e tu és um.')
        break
    elif resposta == 'F':
        print('Vai estudar!')
        break
    else:
        print('Resposta inválida.')
#Cálculo IMC

print('---CÁLCULO IMC---')
peso = float(input('Digite o seu peso atual '))
altura = float(input('Digite a sua altura '))
IMC = peso/(altura*altura)

print('O seu IMC é 'f'{IMC}')
if 0.0 <= IMC <= 18.5:
    print('O seu IMC sugere que está com baixo peso.')
elif 18.5 <= IMC <= 24.9:
    print('PARABÉNS, está com um peso considerado normal pelo IMC.')
elif 25.0 <= IMC <= 29.9:
    print('ATENÇÃO: Sobrepeso, pratique algum exercício para melhorar a sua condição.')
elif 30.0 <= IMC <= 34.9:
    print('OBESIDADE grau 1, consulte um nutricionista o mais breve possível.')
elif 35.0 <= IMC <= 39.9:
    print('OBESIDADE grau 2!')
else:
    print('OBESIDADE MÓRBIDA!!!)')
















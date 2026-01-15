#DESAFIO 44 GUANABARA

print('Prima 1 para vista/cheque;')
print('Prima 2 para vista Cartão')
print('Prima 3 para duas prestações')
print('Prima 4 para três ou mais prestações')
metodo = int(input('Selecione o método de pagamento: '))

produto = 35

vistaCheque = 10
vistaCartao = 5
DuasCartao = 0
TresMais = 20

percentual = 100

if metodo == 1:
    print(f'O produto custar-lhe-à {produto - (produto*vistaCheque/percentual)}€')

elif metodo == 2:
    print(f'O produto custar-lhe-à {produto - (produto*vistaCartao/percentual)}€')

elif metodo == 3:
    print(f'O produto custar-lhe-à {produto - (produto*DuasCartao/percentual)}€')
else:
    print(f'Serão calculados juros à taxa percentual de 20, pelo que o seu produto irá custar-lhe {produto+(produto*TresMais/percentual)}€')


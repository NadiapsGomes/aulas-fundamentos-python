listaCompras = []

detergentes = ['sanitol', 'amaciador']
prodHigiene = ['Dove', 'champô']
alimentacao = ['massa', 'arroz', 'frango']
frutas = ['banana', 'manga', 'nozes']

listaCompras.append(detergentes)
listaCompras.append(prodHigiene)
listaCompras.append(alimentacao)
listaCompras.append(frutas)

print(listaCompras)

prodHigiene.append('toalhitas')
print(prodHigiene)
frutas.remove('banana')
print(listaCompras[1][0]) #imprime o indice da minha lista onde pretendo

for divisao in range(len(listaCompras)): #estou a dividir a minha lista em matrizes
    print(listaCompras[divisao])


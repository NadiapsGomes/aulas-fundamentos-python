maior_idade = menor_idade = 0

for c in range(0, 10):
    idade = int(input('Digite a sua idade: '))
    if c == 0:
        maior_idade = idade
        menor_idade = idade
    else:
        if idade > maior_idade:
            maior_idade = idade

        if idade < menor_idade:
            menor_idade = idade

print(f'Menor idade inserida: {menor_idade}')
print(f'Maior idade inserida: {maior_idade}')
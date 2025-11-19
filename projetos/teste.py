num_linhas = 5
for c in range(0,5): #linha
    for x in range(0,5): #coluna
        if c == x or c + x == num_linhas - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()


# Explicação: o numero de linhas deve ser ímpar para ter um centro bem definido
# uma variável para as linhas outra para as colunas
# se a linha for igual a coluna ou a linha mais a coluna igualar tamanho - 1:
# imprime asterisco nas diagona else imprime espaço em branco

#Len é o comprimento da minha string
#Tuples são imutáveis - depois de declaradas nao admitem redefinição

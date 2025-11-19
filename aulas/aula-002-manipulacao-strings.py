string = 'Pyton e Poderoso'

#Fatiamento de String / String Slicer - aceder às strings através de indíces
print(string[7]) #e
print(string[-1]) #último caracter
print(string[:6]) #Phyton
print(string[9:]) #Poderoso
print(string[::3]) #do inicio ao fim de 2 em 2
print(string[::-1]) #mostra o string ao contrário

#Análise de String / String Analisys
print(len(string)) #tamanho da string
print(string.count('o')) #quantas vezes aparece o
print('Pyton'in string) #Devolve true or false
print(string.find('e')) #Devolve a posição do solicitado
print(string.find('ole')) #nao encontra e devolve
print(string.startswith('Python')) #devolve true or false


#Transformação de String / String Transfiguration
string=input('Digite uma frase')

print(len(string))
print(len(string.strip()))
print(len(string))
print(len(string.rstrip()))
print(string.lower())
print(string.upper())
print(len(string.replace(_old' ', new)
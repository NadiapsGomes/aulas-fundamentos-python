#Informar qual é o caminho do ficheiro

#path(caminho) - vai pegar na variável e dar-lhe funcionalidades diferentes

from pathlib import Path #Classe path que dá métodos/funções típicas de ficheiros


#Criar a variável que representa o caminho do ficheiro

string = r'' #leitura literal, raw string
caminho = Path(r'ficheiros/teste.txt') #o caminho está representado por uma biblioteca path

#O pyhton cria o ficheiro se ele não existir
#Podemos abrir o ficheiro em modos diferentes:
#Modo write 'w'
#Read 'r'
#append 'a'

with caminho.open('w', encoding='utf8', errors='ignore') as file:
    nome = input('Digite o seu nome: ')
    file.write(f'Nome: {nome}\n')

    file.write('Olá turma!\n')
    file.write('Olá novamente!!')






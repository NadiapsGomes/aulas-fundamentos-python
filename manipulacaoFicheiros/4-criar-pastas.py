import os

nome_pasta = 'ficheiros2'

os.mkdir(nome_pasta) #singular - só cria uma pasta

caminho = 'fans/ficheiros'
os.makedirs(caminho,exist_ok=True)




username = input('Digite o seu username: ')
password = input('Escolha uma password: ')

dadosacesso = (username,password)
print(dadosacesso)

if dadosacesso != username or password:
    print('Tente novamente')

elif username and password == dadosacesso:
    print('Login efetuado com sucesso')


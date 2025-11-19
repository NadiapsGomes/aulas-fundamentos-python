#Letícia, ALexandra, Roman, Nádia

print('BEM VINDO CARO UTILIZADOR')
username = input('Por favor digite o seu nome ').strip()
email = input('Indique o seu e-mail ').strip()
password = input('Escolha uma password ')

print(f'{username} o seu egisto foi concluído com sucesso, por favor inicie sessão')

print('[1] LOGIN')
print('[2] SAIR')

opcao=input('Digite uma opção ')

if opcao =="1":
    print(f'Bem vindo, {username}')

    cred1 = input('Digite o seu email ')
    cred2 = input('Insira a sua password ')

if cred1== email and cred2==password:
    print('Login efetuado com sucesso')

else:
    print('Credenciais erradas, por favor tente novamente')
    cred3 = input('Digite o seu email ')
    cred4 = input('Insira a sua password ')

    if cred3!=email or cred4!=password:
        print('CONTA BLOQUEADA')











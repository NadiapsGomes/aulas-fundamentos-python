#Crie uma classe ContaBancaria com atributos titular, saldo e limite.
# Adicione métodos para depositar() e sacar(),
# alterando o saldo da conta de acordo com a operação.

class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor
        print(f'{valor}€ depositado com sucesso. Saldo atual: {self.saldo:.2f}€')

    def levantar(self, valor):
        if valor > self.limite:
            print(f'Só pode levantar até {self.limite}€.')
        elif valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
            print(f'{valor}€ levantados com sucesso. Saldo atual: {self.saldo:.2f}€')

nova_conta = ContaBancaria('Nádia', 4000, 400)

nova_conta.levantar(20)
nova_conta.depositar(100)



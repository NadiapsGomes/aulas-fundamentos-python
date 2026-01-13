from datetime import datetime, timedelta
from time import sleep


class Processo:
    def __init__(self, processo, dataNotificacao, prazo):
        self.processo = processo
        self.dataNotificacao = dataNotificacao
        self.prazo = prazo

    def considera_seCitado(self):
        print('Selecione a forma de citação/notificação:')
        print('[1] - Via postal')
        print('[2] - Por contacto pessoal')
        print('[3] - Via eletrónica')
        print('[4] - Por afixação de edital')
        print('[5] - Por depósito (pessoas coletivas)')
        opcao = int(input('Selecione a opção: '))

        if opcao == 1:
            print('Citado na data de assinatura do AR.')
            return 0
        elif opcao == 2:
            print('Citado no próprio dia.')
            return 0
        elif opcao == 3:
            print('+3, considera-se citado ao terceiro dia (art. 219º nº 6 CPC)')
            return 3
        elif opcao == 4:
            print('Considera-se citado no dia da publicação do anúncio')
            return 0
        elif opcao == 5:
            print('+8, considera-se citado ao oitavo dia (art. 230º nº 2 CPC)')
            return 8
        else:
            print('Opção inválida')
            return 0

    def dilacao(self):
        print('Cumpre ainda aferir uma eventual dilação. Verifique:')
        print('[1] - AR assinado por pessoa diversa do destinatário')
        print('[2] - Tendo ocorrido mediante afixação')
        print('[3] - Correspondência recebida nas regiões autónomas')
        print('[4] - Correspondência recebida no estrangeiro')
        print('[5] - Pessoa coletiva - citação por depósito')
        print('[6] - Nenhuma das anteriores')
        opcaoo = int(input('Selecione a opção: '))

        if opcaoo == 1:
            print('+5 dias (art. 245º nº 1 a) CPC)')
            return 5
        elif opcaoo == 2:
            print('+5 dias (art. 245º nº 1 a) CPC)')
            return 5
        elif opcaoo == 3:
            print('+15 dias (art. 245º nº 2 CPC)')
            return 15
        elif opcaoo == 4:
            print('+30 dias (art. 230º nº 2 CPC)')
            return 30
        elif opcaoo == 5:
            print('+30 dias (art. 229º nº 5 ou 246º nº 4 CPC)')
            return 30
        elif opcaoo == 6:
            return 0
        else:
            print('Opção inválida')
            return 0


processo = input('Digite o número de Processo Judicial: ').upper()
dataNotificacao = input('Data da citação (dd/mm/aaaa): ')
prazo = int(input('Prazo de contestação (dias): '))

dataNotificacao = datetime.strptime(dataNotificacao, '%d/%m/%Y')

novoProcesso = Processo(processo, dataNotificacao, prazo)

print(f'\nProcesso: {processo}')

dias_citacao = novoProcesso.considera_seCitado()
dias_dilacao = novoProcesso.dilacao()

total_dias = prazo + dias_citacao + dias_dilacao
data_final = dataNotificacao + timedelta(days=total_dias)

print(f'O prazo termina em {data_final.strftime("%d/%m/%Y")}\nConsidera-se citado no dia {prazo}, a que acrescentamos a dilação de {dias_citacao + dias_dilacao} dias.\nDispõe ainda de mais 3 dias, caso pretenda suportar a coima referente ao justo impedimento elencada no artigo 139º CPC.')



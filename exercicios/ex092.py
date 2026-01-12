#Crie uma classe Produto com os atributos nome e quantidade em stock.
# Adicione um metodo que mostre o stock no estilo O produto X tem Y unidades em stock.
#  Adicione um novo metodo que aumenta a quantidade de stock numa determinada quantidade.

class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def mostrar_stock(self):
        print(f'O produto {self.nome} tem {self.quantidade} unidades em stock.')

    def aumentar_stock(self, quantidade):
        self.quantidade += quantidade
        print('Novo stock adicionado com sucesso.')

produto1 = Produto('Saias', 3)
produto2 = Produto('Vestidos', 10)
produto3 = Produto('Tops', 15)

produto1.mostrar_stock()
produto1.aumentar_stock(1)
produto1.mostrar_stock()


#Adicione um metodo à classe desenvolvida no exercício anterior Livro que
# imprime uma descrição do livro no formato:
# “O livro com o titulo X foi escrito pelo autor Y".

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def leituras(self):
        print(f'Plano de leitura anual: {self.titulo}, do autor {self.autor}')

    def descricao(self):
        print(f'O livro com o titulo {self.titulo} foi escrito pelo autor {self.autor}.')


Livro1 = Livro('Hábitos Atómicos', 'James Clear')
Livro2 = Livro('Algoritmocracia', 'Adolfo Mesquita Nunes')
Livro3 = Livro('O segredo dos segredos', 'Dan Brown')

Livro1.descricao()
Livro2.descricao()
Livro3.descricao()


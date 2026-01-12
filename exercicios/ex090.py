#Crie uma classe chamada Livro que tenha dois atributos:
# titulo e autor.
# Instancie três objeto dessa classe e imprima os valores dos atributos.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def leituras(self):
        print(f'Plano de leitura anual: {self.titulo}, do autor {self.autor}')


Livro1 = Livro('Hábitos Atómicos', 'James Clear')
Livro2 = Livro('Algoritmocracia', 'Adolfo Mesquita Nunes')
Livro3 = Livro('O segredo dos segredos', 'Dan Brown')

Livro1.leituras()
Livro2.leituras()
Livro3.leituras()


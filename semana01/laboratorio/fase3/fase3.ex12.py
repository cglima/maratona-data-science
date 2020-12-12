"""
Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhecer, engordar, emagrecer, crescer.

Obs: Por padrão, a cada ano que nossa pessoa envelhece,
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

"""

class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura


    def envelhecer(self, idade):
        self.idade = idade

        if idade < 21:
            self.altura = altura + 0.5


    def engordar(self, peso):
        self.peso = peso


    def emagrecer(self, peso):
        self.peso = peso


    def crescer(self, altura):
        self.altura = altura

if __name__ == "__main__":

    pessoa = Pessoa()
    
# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 8.8
# Description:      Resolução do problema livro Perkovic, capítulo 8, pág 285:
#                   Implemente a classe Vetor, que aceita os mesmos métodos da
#                   classe Ponto. Ela deve aceitar também a adição de vetor e
#                   operações de produto
# Site:
# Linkedin:         www.linkedin.com/in/klaytonfacre
# Escrito por:      Klayton Facre
# Mantido por:      Klayton Facre
# -------------------------------------------------------------------------------#
# Usage:
# -------------------------------------------------------------------------------#
# Python Version:
#                   3.0 ou superior
# -------------------------------------------------------------------------------#
# History:          v1.0 25/05/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
class Point:
    'Classe que representa um ponto no plano cartesiano'

    def setx(self, abscissa):
        'Define o valor da coordenada x do ponto'
        self.x = abscissa

    def getx(self):
        'Retorna o valor da coordenada x do ponto'
        return self.x

    def sety(self, ordenada):
        'Define o valor da coordenada y do ponto'
        self.y = ordenada

    def gety(self):
        'Retorna o valor da coordenada y do ponto'
        return self.y

    def get(self):
        'Retorna o valor das coordenadas x e y do ponto, nesta ordem'
        return self.x, self.y

    def move(self, offsetx, offsety):
        'Move o ponto, adicionando os offsets as coordenadas'
        self.x += offsetx
        self.y += offsety

    def __repr__(self):
        'Padroniza a representação do objeto como sendo: (x,y)'
        return '({},{})'.format(self.x, self.y)

    def __init__(self, coordx=0, coordy=0):
        self.x = coordx
        self.y = coordy


class Vetor(Point):

    def __repr__(self):
        'Padroniza a representação do objeto como sendo: Vetor(x,y)'
        return 'Vetor({},{})'.format(self.x, self.y)

    def __add__(self, other):
        'Retorna um novo vetor que é o resultado da soma'
        novo_vetor = Vetor(self.x + other.x, self.y + other.y)
        return novo_vetor

    def __mul__(self, other):
        'Retorna um novo vetor que é o resultado da multiplicação'
        return ((self.x * other.x) + (self.y * other.y))

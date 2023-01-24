# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 8.3
# Description:      Resolução do problema livro Perkovic, capítulo 8, pág 262:
#                   Implemente a classe Retângulo com os métodos solicitados.
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
# History:          v1.0 14/05/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
from curses.ascii import alt


class Retangulo:
    largura = 0
    altura = 0

    def setTamanho(self, larg, alt):
        'Define as dimensões do retângulo, sua largura e altura, nesta ordem.'
        self.largura = larg
        self.altura = alt

    def perimetro(self):
        'Retorna o perímetro do retângulo.'
        return 2 * self.altura + self.largura

    def area(self):
        'Retorna a área do retângulo.'
        return self.largura * self.altura

    def __init__(self, larg, alt) -> None:
        self.largura = larg
        self.altura = alt

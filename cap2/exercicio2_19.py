# -------------------------------------------------------------------------------#
# Program Name:     Exercício 2.19
# Description:      Resolução do problema livro Perkovic, capítulo 2, pág 50:
#
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
# History:          v1.0 01/02/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
import math

raio = 10


def calcula_distancia(coord_x, coord_y):
    'Calcula e retorna a distância do centro (0,0) até as coordenadas informadas (x,y)'
    return math.sqrt(math.pow(coord_x, 2) + math.pow(coord_y, 2))


def acertou(coord_x, coord_y):
    'Verifica e retorna se o lançamento acertou o alvo'
    distancia = calcula_distancia(coord_x, coord_y)
    if distancia < raio:
        return True
    else:
        return False


print('a) (0,0): {}'.format(acertou(0, 0)))
print('b) (10,10): {}'.format(acertou(10, 10)))
print('c) (6, -6): {}'.format(acertou(6, -6)))
print('d) (-7,8): {}'.format(acertou(-7, 8)))

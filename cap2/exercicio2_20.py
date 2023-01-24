# -------------------------------------------------------------------------------#
# Program Name:     Exercício 2.20
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


def altura_alcancada(comprimento, angulo):
    if angulo > 90 or angulo < 0:
        raise ValueError
    else:
        angulo_rad = (math.pi * angulo) / 180
        return comprimento * math.sin(angulo_rad)


print('a) {} pés e {} graus: {:.2f} metros'.format(
    16, 75, altura_alcancada(16, 75)))
print('b) {} pés e {} graus: {:.2f} metros'.format(
    20, 0, altura_alcancada(20, 0)))
print('c) {} pés e {} graus: {:.2f} metros'.format(
    24, 45, altura_alcancada(24, 45)))

# -------------------------------------------------------------------------------#
# Program Name:     Exercício 2.12
# Description:      Resolução do problema livro Perkovic, capítulo 2, pág 48:
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

from statistics import median


acumulador = 0
for index in range(1, 8):
    acumulador += index
print('Resolução da letra a: {}'.format(acumulador))

sara = 65
fatima = 56
mark = 45
media_idade = (sara + fatima + mark) / 3
print('Solução da letra b: {}'.format(media_idade))

print('Solução da letra c: {}'.format(2**20))

print('Solução da letra d: {}'.format(4356//61))

print('Solução da letra e: {}'.format(4365 % 61))

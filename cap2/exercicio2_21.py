# -------------------------------------------------------------------------------#
# Program Name:     Exercício 2.21
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
import string


def reverte(text):
    tamanho = len(text)
    index = -1

    while tamanho + index >= 0:
        print('{}'.format(text[index]), end='')
        index -= 1


texto = input('Digite um texto: ')
reverte(texto)
print()

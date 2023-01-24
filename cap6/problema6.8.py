# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 6.8
# Description:      Resolução do problema, livro Perkovic capítulo 6, pág 194.
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
# History:          v1.0 29/07/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
def char(inicio, fim):
    for item in range(inicio, fim + 1):
        print('{} : {}'.format(item, chr(item)))

# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 5.2
# Description:      Resolução do problema livro Perkovic, capítulo 5, pág 139.
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
# History:          v1.0 22/07/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
from Math import pow


def potencias(limite):
    for expoente in range(1, limite + 1):
        print('{} '.format(pow(2, expoente)), end='')

    print()

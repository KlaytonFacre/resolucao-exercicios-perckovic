# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 5.4
# Description:      Resolução do problema livro Perkovic, capítulo 5, pág 143.
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
def fatorial(numero):
    if numero < 0:
        return 0
    elif numero == 0:
        return 1
    elif numero == 1:
        return 1
    else:
        acumulador = 1
        for index in range(1, numero + 1):
            acumulador *= index

        return acumulador

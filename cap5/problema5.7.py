# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 5.7
# Description:      Resolução do problema livro Perkovic, capítulo 5, pág 146.
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
def xmult(lista1, lista2):
    resultado = []
    for itemExterno in lista1:
        for itemInterno in lista2:
            resultado.append(itemExterno * itemInterno)

    return resultado

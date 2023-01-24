# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 5.3
# Description:      Resolução do problema livro Perkovic, capítulo 5, pág 141.
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
def aritmetica(lista):
    if len(lista) == 1:
        return True
    else:
        delta = lista[1] - lista[0]
        for index in range(len(lista) - 1):
            if (lista[index + 1] - lista[index]) != delta:
                return False
        return True

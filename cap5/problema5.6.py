# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 5.6
# Description:      Resolução do problema livro Perkovic, capítulo 5, pág 144.
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
def divisores(numero):
    lista = []
    for index in range(1, numero + 1):
        if numero % index == 0:
            lista.append(index)
    return lista

# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 5.5
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
def acronimo(frase):
    lista = frase.split()
    sigla = ''
    for palavra in lista:
        sigla = sigla + palavra[0].upper()

    return sigla

# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 6.4
# Description:      Resolução do problema, livro Perkovic capítulo 6, pág 184.
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
# History:          v1.0 24/07/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
def contaPalavra(frase):
    contadores = {}
    frase = frase.split()

    for palavra in frase:
        if palavra in contadores:
            contadores[palavra] += 1
        else:
            contadores[palavra] = 1

    return contadores


def contaPalavra2(frase):
    contadores = {}
    frase = frase.split()

    for palavra in frase:
        if palavra in contadores:
            contadores[palavra] += 1
        else:
            contadores[palavra] = 1

    for item in contadores:
        print('{}\tappears {} {}.'.format(
            item, contadores[item], 'times' if contadores[item] > 1 else 'time'))

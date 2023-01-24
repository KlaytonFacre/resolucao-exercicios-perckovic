# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 7.3
# Description:      Resolução do problema, livro Perkovic capítulo 7, pág 234.
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
# History:          v1.0 01/08/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
def safe_open(arquivo, modo='r'):
    try:
        retorno = open(arquivo, modo)
    except:
        return None

    return retorno

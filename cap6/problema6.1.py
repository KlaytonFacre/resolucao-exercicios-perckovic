# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 6.1
# Description:      Resolução do problema, livro Perkovic capítulo 6, pág 177.
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
def estadoNasc(frase):
    presidentes = {'Barack Hussein Obama II': 'Hawaii',
                   'George Walker Bush': 'Connecticut',
                   'William Jefferson Clinton': 'Arkansas',
                   'George Herbert Walker Bush': 'Massachussetts',
                   'Ronald Wilson Reagan': 'Illinois',
                   'James Earl Carter, Jr': 'Georgia'
                   }

    return presidentes[frase]

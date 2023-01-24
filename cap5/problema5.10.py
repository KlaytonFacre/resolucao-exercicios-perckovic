# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 5.10
# Description:      Resolução do problema livro Perkovic, capítulo 5, pág 152.
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
from math import pow


def juros(taxa):
    prazo = 1
    while pow(1 + taxa, prazo) < 2:
        prazo += 1

    return prazo

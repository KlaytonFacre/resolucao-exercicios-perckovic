# -------------------------------------------------------------------------------#
# Program Name:     Exercício 5.19
# Description:      Resolução dos exercícios, livro Perkovic capítulo 5, pág 164.
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
def emAmbas(lista1, lista2):
    for item in lista1:
        if lista2.count(item) != 0:
            return True

# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 3.10
# Description:      Resolução do problema livro Perkovic, capítulo 3, pág 69:
#                   Implementar a função negativos().
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
# History:
#                   v1.0 13/06/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
def negativos(parametro):
    'Imprime apenas os números negativos do parâmetro passado à função'
    for numero in parametro:
        if numero < 0:
            print(numero)


lista = [4, 0, -1, -3, 6, -9]
negativos(lista)

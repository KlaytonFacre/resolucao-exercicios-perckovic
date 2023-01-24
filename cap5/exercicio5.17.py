# -------------------------------------------------------------------------------#
# Program Name:     Exercício 5.17
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
def dobros(lista):
    tamanho = len(lista)
    for index in range(1, tamanho):
        if lista[index] == 2 * lista[index - 1]:
            print(lista[index])

# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 5.8
# Description:      Resolução do problema livro Perkovic, capítulo 5, pág 147.
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
def bubblesort(lista):
    tamanho = len(lista)
    if tamanho == 1:
        return lista
    else:
        for contador in range(tamanho - 1):
            for index in range(tamanho - 1):
                if lista[index] >= lista[index + 1]:
                    lista[index], lista[index +
                                        1] = lista[index + 1], lista[index]
        return lista

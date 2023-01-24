# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 5.9
# Description:      Resolução do problema livro Perkovic, capítulo 5, pág 150.
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
def soma2D(lista1, lista2):
    numLinhas = len(lista1)
    numColunas = len(lista1[0])
    resultado = []

    for linha in range(numLinhas):
        novaLinha = []
        for coluna in range(numColunas):
            novaLinha.append(lista1[linha][coluna] + lista2[linha][coluna])
        resultado.append(novaLinha)

    return resultado


t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]

print(soma2D(t, s))

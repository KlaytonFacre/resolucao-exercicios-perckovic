# -------------------------------------------------------------------------------#
# Program Name:     Exercício 5.16
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
def indicies(frase, letra):
    tamanho = len(frase)
    retorno = []
    for index in range(tamanho):
        if frase[index] == letra:
            retorno.append(index)

    return retorno

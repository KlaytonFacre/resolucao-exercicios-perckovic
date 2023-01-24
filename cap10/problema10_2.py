# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 10.2
# Description:      Resolução do problema livro Perkovic, capítulo 10, pág 358:
#                   Use o pensamento recursivo para implementar a função recursiva
#                   cheers() que, sobre a entrada inteira n, exibe n strings 'Hip '
#                   seguidos por Hurrah.
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
#                   v1.0 02/06/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#

def cheers(count):
    if count <= 0:
        print('Hurrah!!!')
    else:
        print('Hip ', end='')
        cheers(count - 1)


number = 2                                  # Controle aqui no número de 'Hips'
print('cheers({}):'.format(number))
cheers(number)

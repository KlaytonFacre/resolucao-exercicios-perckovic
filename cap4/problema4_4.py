# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 4.4
# Description:      Resolução do problema livro Perkovic, capítulo 4, pág 104:
#                   Esreva a função par() que toma um inteiro positivo n como
#                   entrada e exibe na tela todos os números entre 2 (inclusive)
#                   e n, que sejam divisíveis por 2 ou por 3.
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
# History:          v1.0 12/07/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
def even(limite):
    for index in range(2, limite + 1):
        if (index % 2 == 0) or (index % 3 == 0):
            print(index, end=', ')
    print('\n')


n = 17
print('Range até n = {}:'.format(n))
even(n)

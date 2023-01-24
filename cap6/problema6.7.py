# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 6.7
# Description:      Resolução do problema, livro Perkovic capítulo 6, pág 194.
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
# History:          v1.0 29/07/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
def codifica(frase):
    molde = '{:3} {:7} {:4} {:7}'
    print(molde.format('Car', 'Decimal', 'Hexa', 'Binário'))
    for letra in frase:
        print('{:3} {:7} {:4X} {:7b}'.format(
            letra, ord(letra), ord(letra), ord(letra)))


while True:
    entrada = input('Digite uma palavra: ')
    codifica(entrada)

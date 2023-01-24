# -------------------------------------------------------------------------------#
# Program Name:     Exercício 4.24
# Description:      Resolução do problema livro Perkovic, capítulo 4, pág 131.
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
# History:          v1.0 15/07/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
def animar(time):
    print('Como se soletra campeão?')
    print('Eu sei, eu sei!')
    for letra in time:
        print(letra.upper() + ' ', end='')
    print('!')
    print('É assim que se soletra campeão!')
    print('Vai, ' + time.capitalize() + '!')

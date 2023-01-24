# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 4.2
# Description:      Resolução do problema livro Perkovic, capítulo 4, pág 102:
#                   Métodos sobre strings.
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

frase = 'It will be a sunny day today'

cont = frase.count('day')
clima = frase.find('sunny')
troca = frase.replace('sunny', 'cloudy')

print(cont)
print(clima)
print(troca)

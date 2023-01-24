# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 3.3
# Description:      Resolução do problema livro Perkovic, capítulo 3, pág 64:
#                   Implementar intruções if-else.
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
#                   v1.0 08/06/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
ano = eval(input('Digite o ano: '))

if ano % 4 == 0:
    print('Pode ser um ano bissexto.')
else:
    print('Definitivamente não é um ano bissexto.')

lista = [14232, 54323, 65323, 90533, 65231]
bilhete = eval(input('Agora digite o número do seu bilhete: '))

if bilhete in lista:
    print('Você ganhou!')
else:
    print('Melhor sorte da próxima vez...')

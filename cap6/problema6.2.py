# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 6.2
# Description:      Resolução do problema, livro Perkovic capítulo 6, pág 178.
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
agenda = {'(123)456-78-90': ['Anna', 'Karenina'],
          '(901)234-56-78': ['Yu', 'Tsun'],
          '(321)908-76-54': ['Hans', 'Castorp']
          }


def agenda_r(lista_telefonica):
    while True:
        numero = input(
            'Digite o número de telefone no formato (xxx)xxx-xx-xx: ')
        if numero in lista_telefonica:
            print(lista_telefonica[numero])
        else:
            print('O número informado não está em uso.')

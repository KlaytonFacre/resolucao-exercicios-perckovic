# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 4.5
# Description:      Resolução do problema livro Perkovic, capítulo 4, pág 106:
#                   Suponha que as variáveis primeiro, último, rua, número, cidade,
#                   estado, codPostal já tenham sido atribuídas. Escreva uma
#                   instrução print que crie uma etiqueta de correspondência.
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
def etiqueta(primeiro, ultimo, rua, numero, cidade, estado, codPostal):
    print('{} {}'.format(primeiro, ultimo))
    print('{} {}'.format(numero, rua))
    print('{}, {} {}'.format(cidade, estado, codPostal))


primeiro, ultimo, rua, numero, cidade, estado, codPostal = 'John', 'Doe', 'Main Street', 123, 'AnyCity8', 'AS', '09876'
etiqueta(primeiro, ultimo, rua, numero, cidade, estado, codPostal)

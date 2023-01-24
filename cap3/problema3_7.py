# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 3.7
# Description:      Resolução do problema livro Perkovic, capítulo 3, pág 69:
#                   Implementar intruções for com a função range.
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
#                   v1.0 13/06/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
print('a) Inteiros de 3 até 12, inclusive este.')
for numero in range(3, 13):
    print(numero)

print('b) Inteiros de 0 até (mas não incluindo) 9, com passo de 2.')
for numero in range(0, 9, 2):
    print(numero)

print('c) Inteiros de 0 até (mas não incluindo) 24, com passo de 3')
for numero in range(0, 24, 3):
    print(numero)

print('d) Inteiros de 3 até (mas não incluindo) 12, com passo de 5')
for numero in range(3, 12, 5):
    print(numero)

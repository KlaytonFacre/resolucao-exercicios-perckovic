# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 10.1
# Description:      Resolução do problema livro Perkovic, capítulo 10, pág 358:
#                   Implemente o método recursivo reverse() que aceita um inteiro
#                   não negativo como entrada e exibe os dígitos de n verticalmente
#                   começando com o dígito de ordem baixa.
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
def reverse(number):
    if number < 10:
        print(number)
    else:
        print(number % 10)
        reverse(number//10)


target = 3124
print(target)
reverse(target)

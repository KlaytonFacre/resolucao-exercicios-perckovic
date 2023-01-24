# -------------------------------------------------------------------------------#
# Program Name:     Exercício 4.23
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
def media():
    frase = input('Digite uma sentença: ')

    palavras = frase.split()
    quantidade = len(palavras)
    acumulador = 0
    for palavra in palavras:
        acumulador = acumulador + len(palavra)

    return (acumulador/quantidade)

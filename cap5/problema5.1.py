# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 5.1
# Description:      Resolução do problema livro Perkovic, capítulo 5, pág 138.
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
# History:          v1.0 22/07/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
from Math import pow


def meuIMC(peso, altura):
    imc = peso / pow(altura, 2)

    if imc >= 25:
        print('Sobrepeso')
    elif imc >= 18.5:
        print('Normal')
    else:
        print('Abaixo do peso')

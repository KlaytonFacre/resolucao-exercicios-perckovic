# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 6.9
# Description:      Resolução do problema, livro Perkovic capítulo 6, pág 198.
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
# History:          v1.0 31/07/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
import random


def advinhe():
    numero = eval(input('Digite um número para o range: '))
    aleatorio = random.randrange(0, numero)
    while True:
        chute = eval(input('Digite o seu chute: '))
        if chute < aleatorio:
            print('Muito baixo.')
        elif chute > aleatorio:
            print('Muito alto.')
        else:
            print('Acertou!')
            break


advinhe()

# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 3.13
# Description:      Resolução do problema livro Perkovic, capítulo 3, pág 80:
#                   Escreva uma instrução em Python que invertam o primeiro e
#                   úlitmo valor de uma lista.
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
# History:          v1.0 14/05/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#

time = ['Ava', 'Eleanor', 'Clare', 'Sarah']
print('Lista original; ', time)

time[0], time[-1] = time[-1], time[0]
print('Lista invertida: ', time)

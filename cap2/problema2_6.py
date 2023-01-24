# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 2.6
# Description:      Resolução do problema livro Perkovic, capítulo 2, pág 29:
#                   Escreva expressões em python para avaliar itens de uma lista.
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
# History:          v1.0 24/05/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#

palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']

primeiro = min(palavras)
ultima = max(palavras)

print('Lista: {}'.format(palavras))
print('Primeira: {}'.format(primeiro))
print('Última: {}'.format(ultima))

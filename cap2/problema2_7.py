# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 2.7
# Description:      Resolução do problema livro Perkovic, capítulo 2, pág 31:
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

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

print('Notas iniciais: {}'.format(notas))
print('Quantidade de notas 7: {}'.format(notas.count(7)))
notas[-1] = 4
print('Notas finais: {}'.format(notas))
print('Nota mais alta: {}'.format(max(notas)))
notas.sort()
print('Notas classificadas: {}'.format(notas))
media = sum(notas) / len(notas)
print('Média das notas: {:.2}'.format(media))

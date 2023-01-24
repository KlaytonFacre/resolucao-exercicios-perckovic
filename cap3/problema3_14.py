# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 3.14
# Description:      Resolução do problema livro Perkovic, capítulo 3, pág 83:
#                   Implemente a função trocaPU() que troca o primeiro e último
#                   elemento da lista passada como argumento.
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
def trocaPU(lista):
    lista[0], lista[-1] = lista[-1], lista[0]


ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']
print('Lista de ingredientes: {}'.format(ingredientes))
trocaPU(ingredientes)
print('Lista após a troca: {}'.format(ingredientes))

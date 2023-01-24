# -------------------------------------------------------------------------------#
# Program Name:     Problema Prático 6.5
# Description:      Resolução do problema, livro Perkovic capítulo 6, pág 186.
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
# History:          v1.0 24/07/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#

def lookup(nome, sobrenome):
    agenda = {('Anna', 'Karenina'): '(123)456-78-90',
              ('Yu', 'Tsun'): '(901)234-56-78',
              ('Hans', 'Castorp'): '(321)908-76-54'
              }
    if (nome, sobrenome) in agenda.keys():
        return agenda[(nome, sobrenome)]
    else:
        return 'Pessoa não encontrada'


while True:
    nome = input('Digite o nome: ')
    sobrenome = input('Digite o sobrenome: ')
    print('{}'.format(lookup(nome, sobrenome)))

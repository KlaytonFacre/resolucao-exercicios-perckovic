# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 4.6
# Description:      Resolução do problema livro Perkovic, capítulo 4, pág 109:
#                   Implemente a função rol(), que recebe ujma lista contendo
#                   informações de estudantes e exibe um rol. Cuide para que o rol
#                   exibido tenha 10 espaços para cada valor de string e 8 para a
#                   nota, incluindo 2 espaços para a parte decimal.
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
def rol(estudantes):
    print('{0:10}{1:10}{2:10}{3:8}'.format(
        'Último', 'Primeiro', 'Classe', 'Nota Média'))
    formato = '{0:10}{1:10}{2:10}{3:8.2f}'
    for pessoa in estudantes:
        print(formato.format(pessoa[0], pessoa[1], pessoa[2], pessoa[3]))


estudantes = [['DeMoines', 'Jim', 'Pleno', 3.45],
              ['Pierre', 'Sophie', 'Pleno', 4.0],
              ['Columbus', 'Maria', 'Sênior', 2.5],
              ['Phoenix', 'River', 'Júnior', 2.45],
              ['Olympis', 'Edgar', 'Júnior', 3.99]]
rol(estudantes)

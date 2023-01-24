# -------------------------------------------------------------------------------#
# Program Name:     Exercício 2.18
# Description:      Resolução do problema livro Perkovic, capítulo 2, pág 50:
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
# History:          v1.0 01/02/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#

flores = ['rosa', 'buganvília', 'iúca',
          'margarida', 'dália', 'lírio dos vales']
print('a) {}'.format(flores))
print('b) {}'.format('batata' in flores))

espinhosas = flores[:3]
print('c) {}'.format(espinhosas))

venenosas = flores[-1:]
print('d) {}'.format(venenosas))

perigosas = espinhosas + venenosas
print('e) {}'.format(perigosas))

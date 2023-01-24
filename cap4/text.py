# -------------------------------------------------------------------------------#
# Program Name:     Exemplo de formatação
# Description:      Transcrição do exemplo da página 109.
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
# History:          v1.0 12/07/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
def taxas_crescimento(n):
    'mostra valoroes para 3 funções usando i = 1,...,n'
    print('i\ti**2\ti**3\t2**i')
    for i in range(2, n+1):
        print('{}\t{}\t{}\t{}'.format(i, i**2, i**3, 2**i))


taxas_crescimento(30)

# -------------------------------------------------------------------------------#
# Program Name:     Exercício 4.25
# Description:      Resolução do problema livro Perkovic, capítulo 4, pág 131.
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
# History:          v1.0 15/07/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
def contaVogal(frase):
    vogais = 'aeiou'
    contagem = [0, 0, 0, 0, 0]
    for letra in frase:
        if letra in vogais:
            contagem[vogais.find(letra)] += 1
    print('a, e, i, o, u aparecem, respectivamente, {}, {}, {}, {}, {} vezes'.format(
        contagem[0], contagem[1], contagem[2], contagem[3], contagem[4]))

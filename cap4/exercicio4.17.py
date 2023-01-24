# -------------------------------------------------------------------------------#
# Program Name:     Exercício 4.17
# Description:      Resolução do problema livro Perkovic, capítulo 4, pág 130.
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
mensagem = 'O segredo desta mensagem é que a mensagem é secreta'
tamanho = len(mensagem)
conta = mensagem.count('secreta')
censurado = mensagem.replace('mensagem', 'xxxxxxxx')

print(mensagem)
print(tamanho)
print(conta)
print(censurado)

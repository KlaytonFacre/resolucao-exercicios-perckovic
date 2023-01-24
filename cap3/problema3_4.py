# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 3.4
# Description:      Resolução do problema livro Perkovic, capítulo 3, pág 64:
#                   Implementar uma estrutura if-else.
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
# History:
#                   v1.0 08/06/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
usuarios = ['joe', 'sue', 'hani', 'sophie']

login = input('Login: ')

if login in usuarios:
    print('Você entrou!')
else:
    print('Usuário desconhecido.')

print('Fim.')

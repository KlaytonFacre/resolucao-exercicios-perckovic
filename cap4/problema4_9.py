# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 4.9
# Description:      Resolução do problema livro Perkovic, capítulo 4, pág 117:
#                   Escreva uma função que aceita duas entradas, um arquivo e
#                   uma string alvo, e retorna as linhas do arquivo que contém a
#                   string alvo
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
def meuGrep(string_alvo, nome_arquivo):
    in_file = open(nome_arquivo, 'r')

    for linha in in_file:
        if (string_alvo in linha):
            print(linha, end='')
        else:
            continue

    in_file.close()


frase = input('Digite a string a ser buscada: ')
alvo = 'example.txt'
meuGrep(frase, alvo)
print('\nFim.')

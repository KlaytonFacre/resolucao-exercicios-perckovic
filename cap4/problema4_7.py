# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 4.7
# Description:      Resolução do problema livro Perkovic, capítulo 4, pág 116:
#                   Escreva uma função que aceita duas entradas de string e retorna
#                   o número de ocorrências da string alvo no arquivo.
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
def busca(string_alvo, arquivo):
    'Busca as ocorrencias de uma string em um arquivo e retorna o número de ocorrencias'
    in_file = open(arquivo, 'r')
    tmp_string = in_file.read()
    in_file.close()

    return str.count(tmp_string, string_alvo)


alvo = input('Digite a string a ser buscada: ')
print('Iniciando a busca de {} no arquivo example.txt'.format(alvo))
counter = busca(alvo, 'example.txt')
print('Foram encontradas {} ocorrencias de \'{}\' em {}'.format(
    counter, alvo, 'example.txt'))

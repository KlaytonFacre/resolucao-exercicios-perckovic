# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 3.22
# Description:      Resolução do problema livro Perkovic, capítulo 3, pág 90:
#                   Implemente um programa que imprime palavras de uma lista mas
#                   não a palavra 'segredo'
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
# History:          v1.0 20/06/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#

# Globais de controle do programa
# Lista de palavras restritas facilmente espansível
palavras_restritas = ['segredo', 'abin']
tamanho_lista = 5


def imprime_lista(lista):
    for palavra in lista:
        if palavra not in palavras_restritas:
            print(palavra)


lista = list()
for index in range(tamanho_lista):
    lista.append(
        input('Digite uma palavra para a lista [{}/{}]: '.format(index + 1, tamanho_lista)))

imprime_lista(lista)

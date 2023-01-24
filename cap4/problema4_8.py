# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 4.8
# Description:      Resolução do problema livro Perkovic, capítulo 4, pág 116:
#                   Escreva uma função que aceita uma entrada, um arquivo, e
#                   retorna a lista de palavras reais, sem símbolos, no arquivo.
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
#                   v1.1 14/07/2022, klayton
#                   - Adicionado o tratamento de erro para o caso de arquivo
#                   inexistente.
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
def busca(nome_arquivo):
    # Símbolos que devem ser buscados e retirados das palavras.
    simbolos = '!,.:;?'
    arquivo = open(nome_arquivo, 'r')
    tmp_string = arquivo.read()
    arquivo.close()

    tmp_list = tmp_string.split()
    final_list = []                     # Lista que conterá as palavras após a sanitização
    for palavra in tmp_list:            # For para realizar a sanitização das palavras contra a lista de símbolos que devem ser retirados
        for caractere in simbolos:
            palavra = palavra.removesuffix(caractere)
        final_list.append(palavra)

    return final_list


alvo = 'example.txt'
try:
    lista = busca(alvo)
except:
    print('Erro! Arquivo não encontrado.')
else:
    print(lista)
    print('Fim.')

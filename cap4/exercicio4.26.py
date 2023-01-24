# -------------------------------------------------------------------------------#
# Program Name:     Exercício 4.26
# Description:      Resolução do problema livro Perkovic, capítulo 4, pág 129.
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
def crypto(nome_arquivo):
    try:
        fd_arquivo = open(nome_arquivo, 'rt')
        buffer_texto = fd_arquivo.read()
        fd_arquivo.close()
    except:
        print('Erro ao ler o arquivo!')
    else:
        texto_cifrado = buffer_texto.replace('secret', 'xxxxxx')
        print(texto_cifrado)


nome_arquivo = input('Digite o nome exato do arquivo: ')
crypto(nome_arquivo)

# -------------------------------------------------------------------------------#
# Program Name:     Get News
# Description:      Programa para tratar páginas WEB. Resolução do problema prático
#                   11.1 do livro do Perckovic, página 408
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
#                   v1.0 22/06/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
from os import system
from urllib.request import urlopen


def news(url, list):
    response = urlopen(url)
    html = response.read()
    html = html.decode()

    for item in list:
        print('{} appears {} time(s).'.format(item, html.count(item)))

    print('End of search. Have a nice day.')


news('http://bbc.co.uk', ['economy', 'climate', 'education', 'weather', 'war'])


# -------------------------------------------------------------------------------#
# Program Name:     Collector
# Description:      Programa para tratar páginas WEB. Aumentando a classe Collector
#                   para coletar dados de texto da WEB. Resolução do problema
#                   prático 11.3 do livro do Perckovic, página 411
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
from re import findall
from urllib.parse import urljoin
from html.parser import HTMLParser
from urllib.request import urlopen


class Collector(HTMLParser):
    'Coleta URLs de hyperlinks em uma página e as coloca em uma lista'

    def __init__(self, url):
        'Inicializa o analisador, o URL e uma lista'
        HTMLParser.__init__(self)
        self.url = url
        self.links = list()
        self.dados = list()

    def handle_starttag(self, tag, attrs):
        'Coleta URLs de hyperlinks em sua forma absoluta'
        if tag == 'a':
            for atributo in attrs:
                if atributo[0] == 'href':
                    # Constrói o URL absoluto
                    absoluto = urljoin(self.url, atributo[1])
                    # Coleta somente links HTTP
                    if absoluto[:4] == 'http':
                        self.links.append(absoluto)

    def getLinks(self):
        'Retorna a lista com os URLs em formato absoluto'
        return self.links

    def handle_data(self, data):
        'Coleta os dados nas tags e armazena em uma lista'
        self.dados.append(data)

    def getData(self):
        for frase in self.dados:
            palavra = str(frase)
            if palavra.isspace:
                self.dados.pop(frase)
            elif palavra.isprintable:
                pass

        return self.dados


response = urlopen('http://www.w3c.org/Consortium/facts.html')
html = response.read().decode()

linkCollector = Collector(html)
linkCollector.feed(html)

print('Links: ')
for link in linkCollector.links:
    print(link)

print('Dados: ')
for frase in linkCollector.dados:
    print(frase)

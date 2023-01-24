# -------------------------------------------------------------------------------#
# Program Name:     MyParser
# Description:      Programa para tratar páginas WEB. Resolução do problema prático
#                   11.2 do livro do Perckovic, página 411
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
from html.parser import HTMLParser
from urllib.request import urlopen


class myHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.tab_counter = 0

    def handle_starttag(self, tag, attrs):
        if tag in ['a']:
            print('{} {} start {}'.format(
                self.tab_counter * '\t', tag, attrs[0][1]))
            self.tab_counter += 1

        elif tag not in ['p', 'br']:
            print('{}{} start'.format('\t' * self.tab_counter, tag))
            self.tab_counter += 1

    def handle_endtag(self, tag: str):
        if tag not in ['p', 'br']:
            self.tab_counter -= 1
            print('{}{} end'.format('\t' * self.tab_counter, tag))


response = urlopen('http://www.w3c.org/Consortium/facts.html')
html = response.read().decode()

linkparser = myHTMLParser()
linkparser.feed(html)

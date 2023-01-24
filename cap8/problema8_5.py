# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 8.5
# Description:      Resolução do problema livro Perkovic, capítulo 8, pág 268:
#                   Modifique o construtor da Classe baralho
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
# History:          v1.0 24/05/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
from random import shuffle


class Carta:
    pass


class Baralho:
    'Representa um baralho de 52 cartas'

    # Valores e naipes das cartas do baralho
    valores = ['2', '3', '4', '5', '6', '7',
               '8', '9', '10', 'J', 'Q', 'K', 'A']
    # Serão 4 símbolos unicode representando os naipes
    naipes = ['\u2660', '\u2661', '\u2662', '\u2663']

    def __init__(self) -> None:
        'inicializa o baralho'
        self.baralho = []

        for naipe in Baralho.naipes:
            for valor in Baralho.valores:
                self.baralho.append(Carta(valor, naipe))

    def distribui_carta(self):
        'Distribui (remove e retorna) a carta do topo do baralho'
        return self.baralho.pop()

    def shuffle(self):
        'Mistura o baralho'
        shuffle(self.baralho)

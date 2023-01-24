# -------------------------------------------------------------------------------#
# Program Name:     blackjack
# Description:      Transcrição do programa para jogar blackjack do Cap 6 do livro
#                   do Percovick.
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
# History:          v1.0 09/08/2022, Klayton
#                   - Start the program
#                   v1.1 10/08/2022, Klayton
#                   - Adicionados mais objetos para representar o jogo
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
from random import shuffle


class Carta:
    'Representa uma carta de jogo de baralho'

    def __init__(self, valor, naipe):
        'Inicializa uma carta com valor e naipe passados ao construtor'
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return '{} {}'.format(self.valor, self.naipe)

    def getValor(self):
        'Retorna o valor da carta'
        return self.valor

    def getNaipe(self):
        'Retorna o naipe da carta'
        return self.naipe


class Baralho:
    'Representa um baralho misturado pronto para o início do jogo'
    naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}
    valores = {'2', '3', '4', '5', '6', '7',
                    '8', '9', '10', 'J', 'Q', 'K', 'A'}

    def __init__(self):
        self.lista = []

        for naipe in self.naipes:
            for valor in self.valores:
                self.lista.append(Carta(valor, naipe))

        shuffle(self.lista)

    def getCarta(self):
        'Retorna o Objeto Carta que está no topo do baralho'
        return self.lista.pop()


class Jogador:

    def __init__(self, nome='Jogador', mao=None):
        self.nome = nome

        if(mao == None):
            self.mao = []
        else:
            self.mao = mao

    def __repr__(self):
        return '{} {}'.format(self.nome, self.mao)

    def __str__(self):
        return '{} {}'.format(self.nome, self.mao)

    def recebeCarta(self, carta):
        self.mao.append(carta)

    def getTotal(self):
        'Retorna o valor da mão de um participante de blackjack.'
        valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                   '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        self.total = 0
        ases = 0

        for carta in self.mao:
            self.total += valores[carta.getValor()]
            if carta.getValor() == 'A':
                ases += 1

        while self.total > 21 and ases > 0:
            self.total -= 10
            ases -= 1

        return self.total

    def getMao(self):
        return self.mao

    def getNome(self):
        return self.nome


def compara_maos(jogador1, jogador2):
    totalJogador1, totalJogador2 = jogador1.getTotal(), jogador2.getTotal()

    if totalJogador1 > totalJogador2:
        print('{} perdeu! {} tem mais pontos[{}].'.format(
            jogador2.getNome(), jogador1.getNome(), jogador1.getTotal()))
    elif totalJogador1 < totalJogador2:
        print('{} venceu com {} pontos!'.format(
            jogador2.getNome(), jogador2.getTotal()))
    else:
        print('Empatou.')


def blackjack():
    baralho = Baralho()

    casa = Jogador('Casa')
    jogador = Jogador('VOCÊ')

    for i in range(2):
        jogador.recebeCarta(baralho.getCarta())
        casa.recebeCarta(baralho.getCarta())

    print(casa)
    print(jogador)

    resposta = input('Deseja (c)arta - default - ou (p)arar? ')
    while resposta in {'', 'c', 'carta'}:
        carta = baralho.getCarta()
        print('Você recebeu {}'.format(carta))
        jogador.recebeCarta(carta)
        print(casa)
        print(jogador)

        if jogador.getTotal() > 21:
            print('Você ultrapassou... perdeu com {} pontos!'.format(
                jogador.getTotal()))
            return

        resposta = input('Deseja (c)arta - default - ou (p)arar? ')

    while casa.getTotal() < 17:
        carta = baralho.getCarta()
        print('A casa recebeu {}'.format(carta))
        casa.recebeCarta(carta)
        print(casa)
        print(jogador)

        if casa.getTotal() > 21:
            print('\nA casa ultrapassou... Você venceu com {} pontos!'.format(
                jogador.getTotal()))
            return

    compara_maos(casa, jogador)


blackjack()

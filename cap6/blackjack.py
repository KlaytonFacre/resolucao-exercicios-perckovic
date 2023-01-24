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
# History:          v1.0 31/07/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
import random


def gera_baralho():
    '''Retorna um baralho misturado pronto para o início do jogo'''
    naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}
    valores = {'2', '3', '4', '5', '6', '7',
               '8', '9', '10', 'J', 'Q', 'K', 'A'}
    baralho = []

    for naipe in naipes:
        for valor in valores:
            baralho.append(valor + ' ' + naipe)

    random.shuffle(baralho)
    return baralho


def distribui_carta(baralho, participante):
    'Retira uma única carta do baralho para o participante especificado.'
    carta = baralho.pop()
    participante.append(carta)
    return carta


def total(participante):
    'Retorna o valor da mão de um participante de blackjack.'
    valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, '1': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    resultado = 0
    ases = 0

    for carta in participante:
        resultado += valores[carta[0]]
        if carta[0] == 'A':
            ases += 1

    while resultado > 21 and ases > 0:
        resultado -= 10
        ases -= 1

    return resultado


def compara_maos(casa, jogador):
    total_casa, total_jogador = total(casa), total(jogador)

    if total_casa > total_jogador:
        print('Você perdeu! A casa tem mais pontos.')
    elif total_casa < total_jogador:
        print('Você venceu com {} pontos!'.format(total_jogador))
    elif total_casa == 21 and 2 == len(casa) < len(jogador):
        print('Você perdeu! A casa tem mais pontos.')
    elif total_jogador == 21 and 2 == len(jogador) < len(casa):
        print('Você venceu com {} pontos!'.format(total_jogador))
    else:
        print('Empatou.')


def display_maos(casa, voce):
    print('Casa: ', end='')
    for carta in casa:
        print(carta, end=' ')
    print()

    print('Você: ', end='')
    for carta in voce:
        print(carta, end=' ')
    print()


def blackjack():
    baralho = gera_baralho()

    casa = []
    jogador = []

    for i in range(2):
        distribui_carta(baralho, jogador)
        distribui_carta(baralho, casa)

    display_maos(casa, jogador)

    resposta = input('Deseja (c)arta - default - ou (p)arar? ')
    while resposta in {'', 'c', 'carta'}:
        carta = distribui_carta(baralho, jogador)
        print('Você recebeu {:>7}'.format(carta))
        display_maos(casa, jogador)

        if total(jogador) > 21:
            print('Você ultrapassou... perdeu.')
            return

        resposta = input('Deseja (c)arta - default - ou (p)arar? ')

    while total(casa) < 17:
        carta = distribui_carta(baralho, casa)
        print('A casa recebeu {:>7}'.format(carta))
        display_maos(casa, jogador)

        if total(casa) > 21:
            print('A casa ultrapassou... Você venceu!')
            return

    compara_maos(casa, jogador)


blackjack()

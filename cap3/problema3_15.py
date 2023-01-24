# -------------------------------------------------------------------------------#
# Program Name:     Problema prático 3.15
# Description:      Resolução do problema livro Perkovic, capítulo 3, pág 84:
#                   Implemente a função olimpiadas(t) que faz com que a tartaruga
#                   t desenhe os anéis olímpicos mostrados. Utilize a função jump().
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
import turtle
import math


def jump(t, x, y):
    'Realiza o salto da tartaruga para a posição (x,y)'
    t.penup()
    t.goto(x, y)
    t.pendown()


def olimpiadas(t):
    raio = 50
    for repeticao in range(5):
        offset_y = 30 * math.pow(-1, repeticao)
        offset_x = -100 + 55 * repeticao
        jump(t, offset_x, offset_y)
        t.circle(raio)


tela = turtle.Screen()
elza = turtle.Turtle()
olimpiadas(elza)
tela.exitonclick()

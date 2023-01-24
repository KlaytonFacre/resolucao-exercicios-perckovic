# -------------------------------------------------------------------------------#
# Program Name:     Programa para desenhar gráfico de função
# Description:      Melhoria do exemplo da pág 70.
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
#                   v1.0 13/06/2022, Klayton
#                   - Start the program
# -------------------------------------------------------------------------------#
# Thanks to:
#
# -------------------------------------------------------------------------------#
import turtle


def f(x):
    'Função que calcula f(x)=x^2 + 1'
    return x**2 + 1


def draw_f(inicio, fim):
    'Função para tentar desenhar o gráfico da função f(x)'
    tela = turtle.Screen()
    elza = turtle.Turtle()
    elza.penup()
    elza.goto(inicio, f(inicio))
    elza.pencolor('blue')
    elza.pendown()
    for dominio in range(inicio, fim):
        elza.goto(dominio, f(dominio))
    tela.exitonclick()


int_esq = eval(input('Digite o limite esquerdo do subdomínio: '))
int_dir = eval(input('Digite o limite direito do subdomínio: '))
draw_f(int_esq, int_dir)

import turtle


def koch(n):
    'Retorna direções turtle para desenhar a curva de Koch'
    if n == 0:
        return 'F'
    else:
        temp = koch(n-1)
        return (temp + 'L' + temp + 'R' + temp + 'L' + temp)


def draw_koch(n):
    tela = turtle.Screen()
    elza = turtle.Turtle()
    directions = koch(n)

    for move in directions:
        if move == 'F':
            elza.forward(300/3**n)
        elif move == 'L':
            elza.lt(60)
        elif move == 'R':
            elza.rt(120)


draw_koch(6)

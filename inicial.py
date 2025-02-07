from turtle import *
from freegames import vector
from math import sqrt

t = Turtle()

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circl(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    r = sqrt((start.x - end.x)**2+(end.y - end.y)**2)
    down()
    begin_fill()
    circle(r)
    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    ancho = (end.x - start.x)/2

    for count in range (2):
        forward(end.x - start.x)
        left(90)
        forward(ancho)
        left(90)

    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('orange'), 'O')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circl), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()

import math
import turtle
def square(x, y, side, angle, color):
    '''
    Function, drawing square
    :param x: upper left corner coordinate X
    :param y: upper left corner coordinate Y
    :param side: side length of a square
    :param angle: the mounting angle of a square
    :param color: color of a square frame and fill
    :return: None
    '''
    turtle.home()
    turtle.up()
    turtle.setposition(x, y)
    turtle.color(color, color)
    turtle.pensize(8)

    turtle.down()
    turtle.right(angle)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.up()

def lines(x, y, length, angle, color):
    '''
    :param x: upper left coordinate X
    :param y: upper left coordinate Y
    :param length: length of line
    :param angle: the mounting angle of a line
    :param color: color of a line
    :return: None
    '''
    turtle.home()
    turtle.up()
    turtle.setposition(x, y)
    turtle.color(color)
    turtle.pensize(1)
    turtle.right(angle)
    q = math.ceil((length/4))

    for i in range(q):
        turtle.down()
        turtle.forward(length)

        # Получить координаты для следующей линии
        a = turtle.xcor() + 4
        b = turtle.ycor()
        turtle.right(180)
        turtle.penup()

        # Позиция черепахи для следующей линии
        turtle.goto(a, b)
        turtle.pendown()
    turtle.up()

def romb(x, y, side, angle, color):
    '''
    Function, drawing square
    :param x: upper left corner coordinate X
    :param y: upper left corner coordinate Y
    :param side: side length of a square
    :param angle: the mounting angle of a square
    :param color: color of a square frame and fill
    :return: None
    '''
    turtle.home()
    turtle.up()
    turtle.setposition(x, y)
    turtle.color(color, color)

    turtle.down()
    turtle.begin_fill()
    turtle.right(angle)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.end_fill()
    turtle.up()

def rectangle(x, y, width, length, angle, color):
    '''
    Function, drawing rectangle
    :param x: upper left corner coordinate X
    :param y: upper left corner coordinate Y
    :param width: side width of a rectangle
    :param length: side length of a rectangle
    :param angle: the mounting angle of a rectangle
    :param color: color of a rectangle frame and fill
    :return: None
    '''
    turtle.home()
    turtle.up()
    turtle.setposition(x, y)
    turtle.color(color, color)

    turtle.down()
    turtle.begin_fill()
    turtle.right(angle)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.end_fill()
    turtle.up()

def triangle90(x, y, side, angle, color):
    '''
    Function, drawing triangle with an angle of 90 degrees
    :param x: upper left corner coordinate X
    :param y: upper left corner coordinate Y
    :param side: length of side of a triangle
    :param angle: the mounting angle of a triangle
    :param color: color of a triangle frame and fill
    :return: None
    '''
    turtle.home()
    turtle.up()
    turtle.setposition(x, y)
    turtle.color(color, color)

    turtle.down()
    turtle.begin_fill()
    turtle.right(angle)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(135)
    turtle.forward(math.sqrt((side ** 2) + (side ** 2)))
    turtle.end_fill()
    turtle.up()

def rapport(x, y, side):
    '''
    Funktion, drawing one fragment of an ornament
    :param x: upper left corner coordinate X
    :param y: upper left corner coordinate Y
    :param side: length of side of a figure
    :param angle: the mounting angle of a figure
    :return: None
    '''
    turtle.speed(10)
    square(x, y, side, 0, '#4ab19c')
    lines(x+5, y-2.5, side-5, 90, '#de584d')
    romb(x+(side/2), y-5, math.sqrt(((side/2)**2)*2) - 5, 45, '#2a6779')

    #начертить 4-конечную звезду
    turtle.up()
    turtle.goto(x+5, y-5)
    turtle.pencolor('#de584d')
    turtle.pensize(5)
    turtle.down()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.goto(x+(side/2), y-(side/4))
    turtle.goto(x+side-5, y-5)
    turtle.goto(x+(0.75*side), y-(side/2))
    turtle.goto(x+side-5, y-side+5)
    turtle.goto(x+(side/2), y-(0.75*side))
    turtle.goto(x+5, y-side+5)
    turtle.goto(x+(side/4), y-(side/2))
    turtle.goto(x+5, y-5)
    turtle.end_fill()

    #начертить диагонали звезды
    turtle.up()
    turtle.goto(x+(side/4), y-(side/2))
    turtle.down()
    turtle.goto(x+(0.75*side), y-(side/2))
    turtle.up()
    turtle.goto(x+(side/2), y-(0.75*side))
    turtle.down()
    turtle.goto(x+(side/2), y-(side/4))
    turtle.up()
    turtle.pensize(1)
    romb(x+(0.375*side), y-(side*0.375), side/4, 0, '#de584d')
    triangle90(x+(0.375*side), y-(side*0.375), math.sqrt(((side/8)**2)*2), 45, '#fb9728')
    triangle90(x+(side*0.625), y-(side*0.625), math.sqrt(((side/8)**2)*2), 225, '#fb9728')

    #Начертить диагонали квадрата
    turtle.goto(x, y)
    turtle.pensize(3)
    turtle.pencolor('#de584d')
    turtle.down()
    turtle.goto(x+side, y-side)
    turtle.up()
    turtle.goto(x+side, y)
    turtle.down()
    turtle.goto(x, y-side)

    #Начертить границы центрального ромба
    turtle.up()
    turtle.goto(x+(0.375*side), y-(side*0.375))
    turtle.down()
    turtle.goto(x+(side*0.625), y-(side*0.375))
    turtle.up()
    turtle.goto(x+(side*0.625), y-(side*0.625))
    turtle.down()
    turtle.goto(x+(0.375*side), y-(side*0.625))
    turtle.up()

def main(x, y, side):
    """Funktion, drawing ornament from 3 fragments"""
    rapport(x, y, side)
    rapport(x+(side+8), y, side)
    rapport(x+((side+8)*2), y, side)
    rapport(x + ((side + 8) * 3), y, side)
    rapport(x + ((side + 8) * 4), y, side)
    rapport(x + ((side + 8) * 5), y, side)
    rapport(x + ((side + 8) * 6), y, side)
    rapport(x + ((side + 8) * 7), y, side)
    rapport(x + ((side + 8) * 8), y, side)
    e = (side+8)*9
    rectangle(x-25, y+25, e+33, 10, 0, '#4ab19c')
    rectangle(x-25, y-side-15, e+33, 10, 0, '#4ab19c')

main(-930, 100, 200)
turtle.done()
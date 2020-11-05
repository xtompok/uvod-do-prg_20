import math
from turtle import forward, left, right, exitonclick, penup, pendown, speed

nx = 4
ny = 3
a = 20


def nakresli_tabulku(nx,ny,a):
    for x in range(nx):
        nakresli_sloupec(ny,a)
        forward(a)

def nakresli_sloupec(ny,a):
    # nakresli sloupec
    for y in range(ny):
        nakresli_ctverec(a)

        # posuň se na další čtverec
        left(90)
        forward(a)
        right(90)
    # vrať se na začátek sloupce
    right(90)
    forward(a*ny)
    left(90)

def nakresli_ctverec(a):
    # nakresli čtverec
    for i in range(4):
            forward(a)
            left(90)
    # nakresli uhlopricky
    left(45)
    forward(a*math.sqrt(2))
    left(135)
    forward(a)
    left(135)
    forward(a*math.sqrt(2))
    right(135)
    forward(a)
    left(180)

speed(0)
nakresli_tabulku(nx,ny,a)

exitonclick()

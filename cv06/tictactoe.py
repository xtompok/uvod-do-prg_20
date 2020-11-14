from turtle import penup, pendown, left, right, forward, setpos, circle, speed, exitonclick, backward
import math

CELL_SIZE = 20

def nakresli_tabulku(nx,ny,a):
    for x in range(nx):
        nakresli_sloupec(ny,a)
        forward(a)
    backward(nx*a)

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


def krizek(a):
    """Nakresli krizek do bunky velikosti a
    Predpoklada, ze stojime v levem dolnim rohu
     a divame se doprava"""
    left(45)
    pendown()
    forward(a*math.sqrt(2))
    penup()
    left(135)
    forward(a)
    left(135)
    pendown()
    forward(a*math.sqrt(2))
    penup()
    right(135)
    forward(a)
    left(180)

def kolecko(a):
    """Nakresli kolecko do bunky velikosti a
    Predpoklada, ze stojime v levem dolnim rohu
     a divame se doprava"""
    forward(a/2)
    pendown()
    circle(a/2)
    penup()
    backward(a/2)

def krizekxy(x,y,a):
    """Nakresli krizek do bunky o souradnicich x,y a velikosti a
    Predpoklada, ze stojime v (0,0) a divame se doprava"""
    forward(x*a)
    left(90)
    forward(y*a)
    right(90)

    krizek(a)

    left(90)
    backward(y*a)
    right(90)
    backward(x*a)

def koleckoxy(x,y,a):
    """Nakresli kolecko do bunky o souradnicich x,y a velikosti a
    Predpoklada, ze stojime v (0,0) a divame se doprava"""
    forward(x*a)
    left(90)
    forward(y*a)
    right(90)

    kolecko(a)
    
    left(90)
    backward(y*a)
    right(90)
    backward(x*a)

speed(0)

nakresli_tabulku(3,3,CELL_SIZE)

hrac = 'X'

while True:
    print(f"Hraje hráč {hrac}")
    coord = input("Zadej souřadnice ve tvaru x y nebo 'k' pro ukončení: ")
    if coord == 'k':
        break
    x = int(coord[0])
    y = int(coord[2])

    if hrac == 'X':
        krizekxy(x,y,CELL_SIZE)
        hrac = 'O'
    else:
        koleckoxy(x,y,CELL_SIZE)
        hrac = 'X'
        

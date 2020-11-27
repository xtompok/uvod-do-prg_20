from turtle import forward, left, right, exitonclick, penup, pendown, speed

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

nakresli_tabulku(2,2,10)
exitonclick()
from turtle import forward, left, right, exitonclick, penup, pendown, speed

nx = 4
ny = 3
a = 20

speed(0)
for x in range(nx):
    for y in range(ny):
        for i in range(4):
            forward(a)
            left(90)

        # posuň se na další čtverec
        left(90)
        forward(a)
        right(90)
    # vrať se na začátek sloupce
    right(90)
    forward(a*ny)
    left(90)
    # posuň se na další sloupec
    forward(a)

penup()
forward(3*a)
pendown()


for x in range(nx):
    for y in range(ny):
        for i in range(6):
            forward(a)
            left(60)

        # posuň se na další čtverec
        left(120)
        forward(a)
        right(60)
        forward(a)
        right(60)
    # vrať se na začátek sloupce
    right(120)
    for y in range(ny):
        forward(a)
        left(60)
        forward(a)
        right(60)
    left(120)
    # posuň se na další sloupec
    forward(a)
    left(60)
    forward(a)
    right(60)

exitonclick()
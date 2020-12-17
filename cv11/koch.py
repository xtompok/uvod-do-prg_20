from turtle import forward, left, right, exitonclick, speed

def koch(delka, uroven):
    # na urovni 1 nakresli lomenou caru
    if uroven == 1:
        forward(delka)
        left(60)
        forward(delka)
        right(120)
        forward(delka)
        left(60)
        forward(delka)
    # na vyssi urovni nakresli misto kazde usecky rekurzivne caru o uroven nizsi
    else:
        koch(delka/3,uroven-1)
        left(60)
        koch(delka/3,uroven-1)
        right(120)
        koch(delka/3,uroven-1)
        left(60)
        koch(delka/3,uroven-1)


speed(0)
# jedno volani nakresli tretinu vlocky
koch(100,3)
right(120)
koch(100,3)
right(120)
koch(100,3)
right(120)

exitonclick()

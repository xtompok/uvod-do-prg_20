from turtle import left, right, forward, backward, speed, exitonclick
from random import uniform

DEG_MIN = 0.3
DEG_MAX = 1
LENGTH_COEFF_MIN = 0.5
LENGTH_COEFF_MAX = 0.8
ANGLE_MIN = 15
ANGLE_MAX = 30

def strom(delka,stupen):
    # Koncová podmínka
    if stupen < 0:
        return
    
    # Nakresli větev
    forward(delka)
    # Otoč se v rozsoše vlevo
    left(30)
    # Nakresli levý podstrom
    strom(delka*0.8, stupen-1)
    # Otoč se zpět
    right(30)
    # Otoč se v rozsoše vlevo
    right(30)
    # Nakresli pravý podstrom
    strom(delka*0.8, stupen-1)
    # Otoč se zpět
    left(30)
    # Vrať se do předchozí rozsochy
    backward(delka)
    
    # V tomto místě je želva na stejném místě stejně natočená,
    # jako byla při vstupu do funkce

def strom_random(delka,stupen):
    """ Draws recursive tree with some randomization

    Reuqired constants:
        DEG_MIN - minimal degree decrement
        DEG_MAX - maximal degree decrement
        LENGTH_COEFF_MIN - minimal shortening of a branch
        LENGTH_COEFF_MAX - maximal shortening of a branch
        ANGLE_MIN - minimal angle at the branching
        ANGLE_MAX - maximal angle at the branching

     """
    if stupen < 0:
        return
    forward(delka)
    angle = uniform(ANGLE_MIN,ANGLE_MAX)
    left(angle)
    strom_random(delka*uniform(LENGTH_COEFF_MIN,LENGTH_COEFF_MAX),
        stupen-uniform(DEG_MIN, DEG_MAX))
    right(angle)
    angle = uniform(ANGLE_MIN,ANGLE_MAX)
    right(angle)
    strom_random(delka*uniform(LENGTH_COEFF_MIN,LENGTH_COEFF_MAX),
        stupen-uniform(DEG_MIN,DEG_MAX))
    left(angle)
    backward(delka)

speed(0)
left(90)

strom(75,5)

right(90)
forward(300)
left(90)

strom_random(100,5)

exitonclick()
import math

def obsah_ctverce(strana):
    return strana*strana

def obsah_obdelnika(a,b):
    return a*b

def obsah_trojuhelnika(strana):
    vyska = strana*math.sqrt(3)/2
    return strana*vyska/2

def obsah_kruhu(polomer):
    return 2*math.pi*polomer

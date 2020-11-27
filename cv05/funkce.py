def obsah_kruhu(r=42):
    """Vrati obsah kruhu o polomeru r"""
    pi = 3.14
    return pi*r*r

def obsah_ctverce(a):
    return a*a

print(obsah_ctverce(3))

if input("C/K?") == 'C':
    funkce = obsah_ctverce
else:
    funkce = obsah_kruhu

# Stejně jako print(obsah_kruhu(4))
print(funkce(4))

exit()


r = 10
a = 12
vysledek = obsah_kruhu(4)
print(r)
print(a)
print(vysledek)


# Udaje z definice funkce
# r = 4
# Telo funkce
# pi = 3.14
# Prirazeni vysledku
# vysledek = pi*r*r

obsah_kruhu(4)

# Udaje z definice funkce
# r = 4
# Telo funkce
# pi = 3.14
# Prirazeni vysledku
# pi*r*r


vysledek = obsah_kruhu()
print(vysledek)


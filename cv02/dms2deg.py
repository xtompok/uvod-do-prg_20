deg = int(input("Zadej stupně: "))
min = int(input("Zadej minuty: "))
sec = float(input("Zadej vteřiny: "))

outdeg = deg+min/60+sec/3600

print("Výsledek:",outdeg,"stupňů")

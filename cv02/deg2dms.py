degf = float(input("Zadej stupně: "))

deg = int(degf)
minf = (degf-deg)*60
min = int(minf)
sec = (minf-min)*60

print("Výsledek:",deg,"stupňů",min,"minut",sec,"vteřin")

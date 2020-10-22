# Hádání čísla

cislo = 42

while True:
    tip = int(input("Tipni si číslo: "))
    if tip == cislo:
        print("Gratuluji, vyhrál jsi!")
        break
    elif tip < cislo:
        print("Tipuj znovu, číslo je větší")
    else: # Není potřeba psát nový elif, protože už zbývá jen jedna možnost
        print("Tipuj znovu, číslo je menší")

print("Díky za hru")

# Úvodní blok s importy
import math

# Načítání / získávání vstupu
a = int(input("Zadej koeficient u x^2: "))
b = int(input("Zadej koeficient u x: "))
c = int(input("Zadej koeficient u 1: "))

# Výpočet
D = b*b-4*a*c
x1 = (-b+math.sqrt(D))/(2*a)
x2 = (-b-math.sqrt(D))/(2*a)

# Výstup
print("Rovnice má kořeny",x1,"a",x2)
# Toto je komentář print(2)

import math

a = int(input("Zadej koeficient u x^2: "))
b = int(input("Zadej koeficient u x: "))
c = int(input("Zadej koeficient u 1: "))

D = b*b-4*a*c
if D > 0:
	x1 = (-b+math.sqrt(D))/(2*a)
	x2 = (-b-math.sqrt(D))/(2*a)
	print("Rovnice má 2 kořeny:",x1,"a",x2)
elif D == 0:
	x = -b/(2*a)
	print("Rovnice má jeden dvojnásobný kořen",x)
else:
	print("Rovnice nemá řešení v oboru reálných čísel")

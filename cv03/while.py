#while True:
#    print("Ahoj")

a = 0
while a < 5:
    a = int(input("Zadej číslo od 5 výše: "))

print(a)

a = 0
while True:
    a = int(input("Zadej číslo od 5 výše: "))
    if a >= 5:
        break

print(a)

# (a >= 0 and a <= 5) or a == 10
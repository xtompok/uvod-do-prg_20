# input vždy vrací str
vstup_str = input("Zadej číslo:")
# pokud potřebujeme jiný typ, je potřeba explicitně výsledek přetypovat
vstup_int = int(vstup_str)

# type vrátí aktuální typ proměnné
print(type(vstup_int))
print(vstup_int+1)

# načtení vstupu a přetypování se dá provést naráz
jiny_int = int(input("Zadej jiné číslo: "))


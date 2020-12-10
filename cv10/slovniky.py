# klic:hodnota

# Vytvoření slovníku
a = {"klic":"hodnota", 5:True, False:42}
print(a)

# Změna hodnoty klíče
a[5] = False
print(a)

# Přidání nového klíče
a["ahoj"]="Test"
print(a)

# Smazání klíče
del a["klic"]
print(a)

# Slovník jako prostředek pro uložení strukturovaných dat
prostredek = {"typ":"tramvaj", 
    "nizkopodlazni":True,
    "cislo": 9001}

print(prostredek)

# Slovník jako překladová tabulka
typy= {1:"vlak",
    2: "metro",
    3: "autobus"}

print(f"Prostredek je {typy[2]}")

# Obyčejný for iteruje přes klíče
for klic in typy:
    print(klic)
    print(typy[klic])

# Lze iterovat přes dvojice (klíč, hodnota)
for (klic, hodnota) in typy.items():
    print(klic)
    print(hodnota)
    typy[klic] = " "+hodnota
print(typy)

# Lze iterovat i jen přes hodnoty
for hodnota in typy.values():
    print(hodnota)

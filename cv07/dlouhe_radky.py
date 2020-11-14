
astr = input("Zadej retezec")
prvni = astr[0].lower()

if prvni == "a" or \
    prvni == "e" or \
    prvni == "o" or \
    prvni == "u" or \
    prvni == "i" or \
    prvni == "y":
    print("Zacina samohlaskou")
else:
    print("Zacina souhlaskou")

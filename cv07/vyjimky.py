from math import sqrt

cislo = None
while cislo is None:
    try:
        cislo = int(input("Zadej cislo: "))
    except ValueError:
        print("Zadal jsi neplatne cislo, opakuj")
print(cislo+1)
    
astr = input("Zadej retezec")
index = input("Zadej index")

def pismeno_na_pozici(astr, index):
    """Vrátí písmeno na pozici index.
    astr i index jsou string"""
    try:
        index = int(index)
        return astr[index]
    except ValueError:
        print("Byl zadan index, ktery neni cislo")
    except IndexError:
        print("Byl zadan index, ktery je mimo retezec")
    except Exception:
        print("Chybička")
    else:
        print("Výjimka nenastala")
    finally:
        print("Provede vždy")

print("Pismeno na pozici:")
print(pismeno_na_pozici("ahoj","0"))
pismeno_na_pozici("ahoj","asdf")
pismeno_na_pozici("ahoj","12")
    


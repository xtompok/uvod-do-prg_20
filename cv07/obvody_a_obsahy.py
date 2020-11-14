from obvody import obvod_ctverce, obvod_trojuhelnika, obvod_obdelnika, obvod_kruhu
import obsahy as o

# čtverec, obdélník, rovnostranný trojúhelník, kruh
typ = input("Zadej typ útvaru: ")
strana = int(input("Zadej délku strany / poloměr: "))

if typ == "ctverec":
    obvod = obvod_ctverce(strana)
    obsah = o.obsah_ctverce(strana)
elif typ == "obdelnik":
    b = int(input("Zadej délku druhé strany: "))
    obvod = obvod_obdelnika(strana,b)
    obsah = o.obsah_obdelnika(strana,b)
elif typ == "trojuhelnik":
    obvod = obvod_trojuhelnika(strana)
    obsah = o.obsah_trojuhelnika(strana)
elif typ=="kruh":
    obvod = obvod_kruhu(strana)
    obsah = o.obsah_kruhu(strana)
else:
    print("Zadal jsi neplatný tvar")
    exit(1)

print(f"Obvod je {obvod} cm")
print(f"Obsah je {obsah} cm^2")

# Převede údaj ve formátu `Ndd mm' ss.sss"` na stupně a výsledek vypíše.
dms = input("Zadej dms: ")
deg = int(dms[1:3])
min = int(dms[4:6])
sec = float(dms[8:-1])

outdeg = deg+min/60+sec/3600

print("Výsledek:",outdeg,"stupňů")

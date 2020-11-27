# rozbalení seznamu nebo ntice
ret = "49 16 34.567"
(stupne, minuty, vteriny) = ret.split(" ")
print(stupne, minuty, vteriny)

# funkce může vracet více věcí, automaticky se z nich udělá ntice
def funkce():
    return 1,True

print(funkce())

# enumerate vyrobí pro každý prvek seznamu dvojici (index,prvek)
flist = ["jedna","dva", "ctyri"]
for idx,prvek in enumerate(flist):
    print(f"Na pozici {idx} je prvek {prvek}")
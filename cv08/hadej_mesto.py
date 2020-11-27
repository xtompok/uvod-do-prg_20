import random
# načtu ze souboru mesta.txt do seznamu názvy měst
#  - nezapomenu oříznout bílé znaky
mesta = []
with open("mesta.txt") as f:
  for m in f:
    mesta.append(m.rstrip())

# ze seznamu vyberu náhodné město
mesto = random.choice(mesta)
print(mesto)

# vyrobím seznam `uhadnuto`
#  - stejné délky jako hádané město
#  - obsahuje samé False"""
uhadnuto = []
for _ in mesto:
  uhadnuto.append(False)
# alternativně lze na jednom řádku:
# uhadnuto = [False] * len(mesto)
print(uhadnuto)

# dokud není uhádnuto
while False in uhadnuto:
  # vypíši aktuální stav hádání
  #  - znaky, jejichž pozice je v seznamu `uhadnuto` True, vypíši
  #  - místo ostatních napíši podtržítka"""
  for i in range(len(uhadnuto)):
    if uhadnuto[i] == True:
      print(mesto[i],end="")
    else:
      print("_",end="")
  print()

  # zeptám se uživatele na písmeno
  pismeno = input("Zadej pismeno: ")

  # procházím hledané jméno
  #  - ty pozice v `uhadnuto`, kde se aktuálně hádané písmeno shoduje s písmenem
  #    ve jméně, přepnu v `uhadnuto` na True
  for i,znak in enumerate(mesto):
    if pismeno == znak.lower():
      uhadnuto[i] = True

# pokud `uhadnuto` obsahuje jen samé True, tak program skončí."""
print(mesto)
print("Gratuluji, vyhral jsi.")


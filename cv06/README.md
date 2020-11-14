# Poznámky z 6. cvičení

None - typ, který značí *nic*

`turtle.setpos` - přesune želvu na dané souřadnice
`turtle.penup` - zvedne tužku
`turtle.pendown` - položí tužku

Pokud potkáte chybu `turtle.Terminator`, tak jste pravděpodobně někde dříve zavolali `exitonclick()` a tudíž není kam kreslit.

Ve funkcích nikdy nepoužívejte proměnné, které jste si buď nedefinovali ve funkci, nebo které nemáte v seznamu argumentů v hlavičce funkce.

## Git
`git clone <URL>` - zkopíruje online repozitář k vám na počítač
`git push` - nahraje commity do online repozitáře
`git pull` - stáhne commity z online repozitáře k vám

## Příklady
### Příklad 1
Napište Tic-tac-toe.
Program vykreslí tabulku 3x3 políčka.
Následně se pořád dokola ptá střídavě prvního a druhého hráče na souřadnice. Pokud některý z hráčů zadá místo souřadnice `k`, program skončí. 
Po zadání souřadnic program na zadaných souřadnicích nakreslí
  - křížek, pokud táhnul první hráč
  - kolečko, pokud táhnul hráč druhý
Souřadnice jsou z rozsahu 0,1,2 pro x i y.
#### Nápověda k postupu:
 - umím nakreslit tabulku?
 - umím nakreslit kolečko?
 - umím nakreslit křížek?
 - umím nakreslit kolečko/křížek na zadaných souřadnicích?
 - umím načíst od uživatele vstup?
 - umím ho převést na číslo?
 - umím to dělat opakovaně?
 - jak ukončím nekonečný cyklus?

# Poznámky z 12. cvičení

## Převod souřadnicových systémů
Modul PyPROJ [dokumentace](https://pyproj4.github.io/pyproj/stable/examples.html)

### Příklad 0
Nainstalujte si PyPROJ (`pip install pyproj`)

## GeoJSON
[specifikace](https://tools.ietf.org/html/rfc7946)

## Příklady 
### Příklad 1 - kreslení stromů rekurzí
Napište program, který rekurzivně nakreslí strom s délkou kmene `delka` a stupněm `stupen`, tedy:
 - pokud je stupeň 0, nic nekreslí a ihned vrátí
 - nakreslí větev délky `delka`
 - otočí se o 60 stupňů vlevo
 - nakreslí reukrzivně podstrom
     - základní délka je `delka/2`
     - stupeň o 1 nižší
 - otočí se zpět
 - otočí se o 60 stuňů vpravo
 - nakreslí reukrzivně podstrom
     - základní délka je `delka/2`
     - stupeň o 1 nižší
 - otočí se zpět
 - zacouvá zpět do výchozího bodu
 Na obdobném principu pracují L-systémy, pomocí kterých lze generovat stromy, listy, domy apod.
 
 ### Příklad 1a
  - zkuste volit zkrácení náhodně z nějakého intervalu
  - zkuste volit úhel náhodně z nějakého intervalu
  - zkuste snižovat stupeň s nějakou pravděpodobností

# Poznámky z 8. cvičení

## Kódování znaků:
 - základní tabulka ASCII
 - čeština ve Windows - `windows-1250`
 - čeština v Unixu - `iso-8859-2`
 - univerzální Unicode - `utf-8` 

`open('<jmeno_souboru>', encoding="windows-1250")`

`str.rstrip()` - ořízne bílé znaky zprava (tzn. mezery, tabulátory, zalomení řádku)
`str.strip()` - ořízne bílé znaky z obou stran


## Příklady

### Příklad 1:
Vytvořte textový soubor s nějakým obsahem a pomocí Pythonu jeho obsah vypište.
Nezapomeňte se před spuštěním programu přepnout do adresáře, kde se soubor nachází.

### Příklad 2:
Napište program, který přečte soubor v kódování windows-1250 a zapíše ho v kódování utf-8.

### Příklad 3:
Napište hru "Hádej město". V souboru mesta.txt je na každé řádce název jednoho města. Program jedno město náhodně vybere a napíše jeho jméno pomocí podtržítek, tzn. za každý znak ve jméně města jedno podtržítko, mezera jako mezera. Následně se ptá na písmena a pokud písmeno ve jménu města je, tak ho doplní místo pomlčky, pokud není, tak zvedne počítadlo chyb. Po uhádnutí města program vypíše počet chybných písmen.

Př.
```
<program si vybral Brno>
____ 
Zadej znak: o
___o
Zadej znak: e
___o
Zadej znak: b
b__o
Zadej znak: r
br_o
Zadej znak: n
brno
Gratulujeme, zvládli jste uhádnout brno s 1 chybami.
<program skončí>
```

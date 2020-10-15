# Poznámky z 2. cvičení

## Operátory:
```python
a // b # celočíselné dělení (dolní celá část z a/b)
a % b # zbytek po dělení a//b. Při dělení 1 vrací desetinnou část (<1)
a < b
a > b
a == b
a != b
a <= b
a >= b
```

## Typy:
`bool` - boolean, může nabývat hodnoty `True` nebo `False`

## Konstrukce if:
```python
if <výraz>:
   # provede se, pokud je <výraz> pravdivý
elif <výraz2>:
   # provede se, pokud je <výraz> nepravdivý a <výraz2> pravdivý
else:
   # provede se, pokud je <výraz> i <výraz2> nepravdivý
```

## Funkce:
Funkce print nic nevrací, nemá smysl ji do něčeho přiřazovat

## Kreslení v Pythonu:
Modul turtle

## Kvadratická rovnice
```
x_1,2 = (-b +- sqrt(D))/(2a)
D = b^2-4ac
```
```python
D = b*b - 4*a*c
```
Pro D > 0 jsou 2 kořeny
Pro D == 0 je jeden dvojnásobný kořen
Pro D < 0 rovnice nemá v R žádné řešení

## Příklady

### Příklad 1:
Upravte program tak, aby se postupně zeptal na koeficient u x^2, x a 1 a následně spočetl kořeny

Př:
Zadej koeficient u x^2: 1
Zadej koeficient u x: 2
Zadej koeficient u 1: 1
Kořeny jsou: -1 a -1

### Příklad 2:
Napište program převádějící formát DMS na desetinné stupně.
Uživatel zadá stupně (int), minuty (int) a vteřiny (float) a program vypíše, kolik je to stupňů (float)

Př:
Zadej stupně: 12
Zadej minuty: 30
Zadej vteřiny: 0
Výsledek: 12.5 stupňů

### Příklad 3:
Jako příklad 2, ale naopak (stupně -> DMS)

### Příklad 4:
Upravte program na výpočet kořenů kvadratické rovnice tak, aby vypsal počet kořenů a pak jejich hodnoty.
Př. 
Pro x^2+1 vypíše: "Rovnice nemá žádný reálný kořen"
Pro x^2+2x+1 vypíše: "Rovnice má jeden dvojnásobný kořen -1"
Pro x^2+4x+3 vypíše: "Rovnice má dva kořeny: <x1> a <x2>"

### Příklad 5:
zkuste si želvu

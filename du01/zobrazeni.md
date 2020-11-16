# Nápověda k zobrazením
V následujících rovnicích označujme zeměpisnou délku jako λ, zeměpisnou šířku jako φ. 
Úhly uvažujeme vždy v radiánech, tedy 180 stupňů = π rad. Poloměr Země v daném
měřítku budeme značit `R`.

## Azimutální zobrazení
Zobrazujeme na rovinu. Rovnoběžky budou vypadat jako soustředné kružnice, pro některá
zobrazení může jít poloměr kružnic do nekonečna. Poledníky budou paprsky
vycházející ze středu kružnic k okrajům pod úhlem `ε=λ`. Pro kružnice tedy potřebujeme určit
jejich poloměr `ρ`, pro poledníky jen délku paprsku, což ale odpovídá největší
zobrazené kružnici + případný přesah, pokud jsou za poslední zobrazenou kružnicí
ještě nějaké další. 

Referenčním bodem je střed kružnic.

### Gnómonická projekce
 - `ρ = R*tg(π -φ)`

### Stereografická projekce
 - `ρ = 2*R*tg((π -φ)/2)`

### Ortografická projekce
 - `ρ = R*sin(π -φ)`

### Lambertovo zobrazení azimutální
 - `ρ = 2*R*sin((π -φ)/2)`

### Postelovo zobrazení
 - `ρ = R*(π -φ)`

## Válcová zobrazení
Zobrazujeme na válec, který omotává, nebo protíná Zemi. Rovnoběžky a poledníky
tvoří síť navzájem kolmých čar, pro některá zobrazení může jít vzdálenost
rovnoběžek od rovníku k nekonečnu. Vzdálenost rovnoběžky od rovníku udává `y`,
vzdálenost poledníku od nultého poledníku udává `x`. 

Referenčním bodem je průsečík nultého poledníku a rovníku.

### Marinovo zobrazení
 - `x = R*λ`
 - `y = R*φ`

### Lambertovo zobrazení válcové
 - `x = R*λ`
 - `y = R*sin(φ)`

### Braunovo zobrazení
 - `x = R*λ`
 - `y = 2*R*tg(φ/2)`

### Mercatorovo zobrazení
 - `x = R*λ`
 - `y = R*ln(cotg(φ/2))`

### Behrmannovo zobrazení
 - `u0 = 30° = π/6`
 - `x = R*λ*cos(u0)`
 - `y = R*sin(φ)*1/cos(u0)`

### Gallovo zobrazení
 - `u0 = 45° = π/4`
 - `x = R*λ*cos(u0)`
 - `y = R*(1+cos(u0))*tg(φ/2)`

### Čtvercové plochojevné
 - `cos(u0) = sqrt(2/π)`
 - `x = R*λ*cos(u0)`
 - `y = R*sin(φ)*1/cos(u0)`

## Kuželová zobrazení
Zobrazujeme na kužel nasazený na Zemi, nebo zemi protínající. Rovnoběžky
vypadají jakou soustředné kruhové oblouky, poledníky jako paprsky vycházející ze
středu oblouků pod úhlem `ε`. V případě, že se pól nezobrazí na bod, jsou
začínají poledníky až od oblouku reprezentujícího pól.  Pro oblouky potřebujeme
určit, jakou část kružnice budou oblouky tvořit (0 - nic, 1 - celá kružnice),
označujeme `n` a poloměr oblouhu, označujeme `ρ`. Poledníky začínají na oblouku
reprezentujícím pól a končí na posledním oblouku. 

Referenční bod je střed oblouků.

### Ptolemaiovo zobrazení
 - `φ0 = 30° = π/6`
 - `n = cos(π-φ0)`
 - `ε = λ*n`
 - `ρ = R*tg(φ0) + R*(φ0-φ)`

### Lambertovo zobrazení kuželové
 - `φ0 = 30° = π/6`
 - `n = (cos((π-φ0)/2))**2`
 - `ε = λ*n`
 - `ρ = 2R*sin(φ/2)/cos(φ0/2)`

## Nepravá zobrazení
Nemají pěknou geometrickou reprezentaci. V našem případě budeme souřadnice
počítat v rovině a to tak, často, aby výsledné lomené čáry připomínaly hledané
křivky.

### Sansonovo zobrazení
 - `x = R*λ*cos(φ)`
 - `y = R*φ`

### Werner-Stabovo zobrazení
 - `E = λ*cos(φ)/R`
 - `x = R * sin(E)`
 - `y = -R*cos(E)`
  - referenční bod je severní pól (má souřadnice po převedení 0,0)

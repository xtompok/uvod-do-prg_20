# Domácí úkol 2 - vzdálenost ke kontejnerům na tříděný odpad

## Motivace
Chcete zhodnotit, jak jsou dostupné kontejnery na tříděný odpad v jednotlivých
čtvrtích. Proto chcete vědět, jaká je průměrná a maximální vzdálenost k
nejbližšímu kontejneru na tříděný odpad pro obyvatele dané čtvrti.

## Zadání
Pro zvolenou množínu adresních bodů a množinu kontejnerů na tříděný odpad
zjistěte průměrnou a maximální vzdálenost k nejbližšímu veřejnému kontejneru na
tříděný odpad. Pro každý adresní bod tedy určete nejbližší veřejný kontejner na
tříděný odpad a následně z těchto vzdáleností spočtěte průměr a maximum. Průměr
a maximum vypište, pro maximum vypište i adresu, která má nejbližší veřejný
kontejner nejdále. 

### Vstupní data
Vstupními daty budou 2 soubory GeoJSON. První obsahuje adresní body zvolené
čtvrti ve WGS-84, lze jej stáhnout z [Overpass
Turbo](http://overpass-turbo.eu/s/11rE) pomocí Exportovat -> Stáhnout jako
GeoJSON. V atributu `addr:street` naleznete jméno ulice, v atributu
`addr:housenumber` naleznete číslo orientační / číslo popisné. Soubor po stažení
pojmenujte `adresy.geojson` a pod tímto jménem ho program také bude načítat.

Druhý soubor obsahuje souřadnice kontejnerů na tříděný odpad, lze jej stáhnout z
[pražského Geoportálu](https://www.geoportalpraha.cz/cs/data/otevrena-data/8726EF0E-0834-463B-9E5F-FE09E62D73FB)
v S-JTSK. Každý kontejner obsahuje v atributu `STATIONNAME` adresu, kde se
nachází a v atributu `PRISTUP`, zda je veřejně přístupný, nebo je přístupný
pouze obyvatelům domu. Soubor po stažení pojmenujte `kontejnery.geojson` a pod
tímto jménem ho také program bude načítat.

### Výstup
Program vypíše, jaká je pro zvolenou množinu adres průměrná vzdálenost k
veřejnému kontejneru na tříděný odpad a ze které adresy je to k nejbližšímu
veřejnému kontejneru nejdále a jak daleko (v metrech, zaokrouhleno na cele
metry). Kontejnery, které jsou přístupné pouze obyvatelům domu nebudeme v
základní verzi uvažovat. Dále program může, ale nemusí, vypsat statistické
údaje o vstupních souborech, jako je počet adres a počet kontejnerů, tyto údaje
by měly být stručné a jasné a nic dalšího by program neměl vypisovat (pokud to
nepožaduje nějaký bonus).

#### Příklad výstupu 
```
Nacteno 265 adresnich bodu.
Nacteno 29 kontejneru na trideny odpad.

Prumerna vzdalenost ke kontejneru je 231 m.
Nejdale ke kontejneru je z adresy Nová ulice 37/4 a to 549 m.
```

### Další požadavky
Program by se měl vypořádat s nekorektním vstupem, jako je vadný nebo chybějící
vstupní soubor. Dále by program měl skončit s chybou, pokud pro některou adresu
je nejbližší kontejner dále než 10 km (může skončit ihned, nemusí dokončit
výpočet). Pokud je soubor validní JSON, ale nevalidní GeoJSON, nebo chybí nějaký
atribut, je v základní verzi v pořádku, že program spadne. 

## Doporučení
Doporučený průběh programu:
 - načtení vstupních souborů
 - výběr jen veřejných kontejnerů
 - převedení souřadnic adresních bodů na S-JTSK pomocí PyProj
 - nalezení nejbližšího kontejneru pro každý adresní bod
 - výpis průměrné a maximální vzdálenosti

Napište si funkce na jednotlivé kroky, případně si rozdělte kroky na podkroky a
opět si na ně napište funkce.

Testujte program nejen na korektní, ale i na nekorektní vstupy. Při předčasném
odevzdání se převážně zaměřuji na ty problémy, které si neumíte snadno odhalit sami.

Přečtěte si [doporučení k minulému úkolu](../du01/README.md), zůstávají stále
platná.

Vizualizujte si průběh programu. Ať už pomocí želví grafiky (funkce
[`setworldcoordinates`](https://docs.python.org/3/library/turtle.html#turtle.setworldcoordinates)
vám může velmi usnadnit práci), nebo pomocí exportu do GeoJSONu a následném
zobrazení např. v QGISu nebo využijte [online GeoJSON prohlížeč](https://geojson.io). 

Převeďte si souřadnice do S-JTSK, v S-JTSK můžete počítat vzdálenost snadno
pomocí Pythagorovy věty.

## Odevzdání
Odevzdávat budete zdrojový kód projektu a soubor s dokumentací. Vše
bude zabalené v zip souboru, který bude obsahovat adresář `du2_jmeno_prijmeni`,
ve kterém bude soubor se zdrojovým kódem a soubor s dokumentací, tedy například:
```
du2.zip
|
\du2_tomas_pokorny
  |- README.md
  \- du2.py
```
Zip archiv mi pošlete mailem. 

Deadline bude 5.1.2021 8.03. Úkoly odeslané po deadlinu budou brány jako neodevzdané. Pokud
odevzdáte úkol vícekrát, budu hodnotit poslední odevzdání před deadlinem.
Každému, kdo mi pošle úkol, odpovím, že jsem ho přijal a že se mi podařilo zip
rozbalit. Pokud neodpovím, urgujte.

Detaily pro odevzdání přes GitHub viz sekce *Odevzdání přes GitHub*.

### Předčasné odevzdání
Pokud odevzdáte úkol dopředu, zkusím se na něj podívat a napsat vám případné
nedostatky. Tato možnost není garantovaná, ale budu se snažit odbavovat úkoly co
nejrychleji. Zaručuji vám pouze to, že na úkoly se budu dívat v tom pořadí, v
jakém mi budou doručeny. Rovněž nezaručuji, že najdu v programu všechny chyby
napoprvé, tudíž pokud si nějaké nevšimnu, není to garance, že máte program
správně, závazné je pouze hodnocení po deadlinu. Pokud budete odevzdávat přes
GitHub, chyby vám vystavím jako Issue.

## Bodování
 * 5 b za funkční aplikaci
 * 3 b za kvalitu kódu
 * 2 b za dokumentaci

Kvalita kódu nyní zahrnuje i komentáře v kódu, více o jednotlivých kategoriích v
minulém zadání.

## Bonusové body

### Používání Gitu pro vývoj (1 b)
Pokud budete pro verzování používat Git, vytvořte si účet na GitHubu nebo jiné
podobné stránce a úkol můžete odevzdat přes něj. Kromě samotného odevzdání je
třeba, aby byl repozitář používán i pro vývoj, tedy by měl obsahovat průběžně
commitovanou práci. Repozitář by měl obsahovat jak program, tak případný soubor
s dokumentací, za hodnocenou verzi se počítá poslední commit pushnutý na GitHub
před deadlinem. Repozitář nemusí, ani by neměl, obsahovat velká vstupní data.
Pokud budete potřebovat pomoct, pište mi.

### Medián (1 b)
Kromě průměrné vzdálenosti ke kontejneru vypište i [medián](https://cs.wikipedia.org/wiki/Medi%C3%A1n) vzdálenosti ke kontejneru. 

### Přiřazení kontejnerů k adresám (3 b)
Program vytvoří soubor `adresy_kontejnery.geojson` ve formátu GeoJSON, který
bude obsahovat všechny adresní body ze vstupních dat a v atributech každého
adresního bodu bude v klíči `kontejner` uloženo `ID` nejbližšího kontejneru k
danému adresnímu bodu.  

### Uvažování domovních kontejnerů (2 b)
Pro adresní body, které mají vlastní kontejner (v klíči `PRISTUP` je uvedeno, že
jsou přístupné jen obyvatelům domu) program nebude hledat nejbližší kontejner a
do průměru a dalších statistik je započte, jako by měly vzdálenost k nejbližšímu
kontejneru rovnou nule. 

### Soubory jako parametry programu (1 b)
Pokud program dostane při spuštění parametr `-a <nazev_souboru>`, bude brát
adresní body z tohoto souboru, pokud dostane parametr `-k <nazev_souboru>`, bude
brát kontejnery z tohoto souboru.  Může dostat žádný, jeden nebo 2 paramtery,
pokud některý parametr není specifikován, zkusí otevřít soubor jména ze zadání. 
Doporučuji využít modulu [`argparse`](https://docs.python.org/3/library/argparse.html)
nebo modulu [`click`](https://click.palletsprojects.com/en/7.x/).

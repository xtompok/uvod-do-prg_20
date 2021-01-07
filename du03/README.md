# Domácí úkol 3 - dělení lomených čar

## Motivace
Dostanete síť liniových prvků, například silnic, a chcete zajistit, aby data
neobsahovala příliš dlouhé úseky mezi body, například proto, že se pak náročněji
počítají kolize (Pokud chci zjistit, jestli se daná úsečka s něčím kříží a nemám
omezenou délku segmentu, tak musím projít všechny ostatní úsečky a nestačí mi se
jen podívat po okolí.).

## Terminologie
 - *segment* - úsečka spojující 2 body
 - *lomená čára* - množina na sebe navazujících segmentů, může být uzavřená
   (poslední a první bod jsou stejné), nebo otevřená (poslední a první bod se
   liší)

## Zadání
Zvolenou množinu lomených čas (linestring) upravte tak, aby neobsahovala
segmenty delší, než je zvolená vzdálenost. K úpravě použijte následující
algoritmus:
 - pokud je segment kratší než zvolená vzdálenost, nechej ho tak
 - pokud je segment delší než zvolená vzdálenost, rozděl ho uprostřed na 2
   stejně dlouhé segmenty a na každý z nich aplikuj tento algoritmus

Pro reprezentaci bodů, segmentů a lomených čar zvolte vhodnou reprezentaci
pomocí tříd, třída reprezentující lomenou čáru by měla mít metodu
`divide_long_segments(max_length)`, která aplikuje výše popsaný algoritmus na sebe, třída
reprezentující segment by měla mít metodu `divide(max_length)`, která vrátí
lomenou čáru vzniklou aplikací výše uvedeného algoritmu na daný segment.

Třídy budou definovány v samostatném modulu / modulech, hlavní program je bude
z těchto modulů importovat.

### Vstupní data
Vstupními daty bude soubor GeoJSON, který bude obsahovat
`FeatureCollection` obsahující jednotlivé `Features` s geometrií typu
`LineString`y. Soubor bude v metrickém souřadnicovém systému (např. S-JTSK),
tedy vzdálenost lze počítat přímočaře Pythagorovou větou. 

Jméno vstupního souboru bude zadáno jako parametr při spouštění skriptu `-f
<nazev_souboru>`, maximální vzdálenost bude zadána jako parametr `-l` při
spouštění skriptu. Pro získání parametrů doporučuji využít modulu
[`argparse`](https://docs.python.org/3/library/argparse.html) nebo modulu
[`click`](https://click.palletsprojects.com/en/7.x/).

Alternativně může program brát vstupní soubor ze souboru `lines.geojson` a
maximální vzdálenost mít definovanou jako konstantu v hlavním programu, ale
toto řešení bude penalizováno -2 body.

### Výstup
Výstupem bude soubor GeoJSON, který bude obsahovat `FeatureCollection`
obsahující jednotlivé `Feature` s geometrií typu `LineString`, která bude
upravená výše popsaným algoritmem. Všechny `properties`, které měla daná `Feature`
ve vstupním souboru, by měly být zachovány i ve výstupním souboru.

Jméno výstupního souboru bude zadáno jako parametr při spouštění skriptu `-o
<nazev_souboru>`.

Alternativně může program zapisovat výstup do souboru `output.geojson`, toto
řešení bude penalizováno -1 bodem.

#### Příklad spuštění programu 
```
python3 divide_linestrings.py -f vstup.geojson -o vystup.geojson -l 30
```

### Další požadavky
Program by se měl vypořádat s nekorektním vstupem, jako je vadný nebo chybějící
vstupní soubor. Pokud je soubor validní JSON, ale nevalidní GeoJSON, nebo chybí nějaký
atribut, je v pořádku, že program spadne. 

## Doporučení
Zkuste si prvně nakreslit na papír, jak budou jednotlivé třídy vypadat, jaké
budou mít objekty atributy a jak budou navzájem propojené. 

Postup "nejprve si to všechno napíšu do jednoho souboru a pak teprve budu
vyrábět třídy a funkce do nich přesouvat" také funguje, ale je pracnější a
náchylnější na zanesení chyb. 

Testovací data si můžete stáhnout například z
[Geoportálu](https://www.geoportalpraha.cz/cs/data/otevrena-data/0AF6DE97-68B3-4CD6-AE5D-76ACEEE50636).

Přečtěte si [doporučení k minulému úkolu](../du02/README.md), zůstávají stále
platná.

Pokud si s nějakou částí nejste jisti, nefunguje vám nebo máte jiný problém,
neváhejte se ozvat, rád vám pomohu.


## Odevzdání
Odevzdávat budete zdrojový kód projektu a soubor s dokumentací. Vše
bude zabalené v zip souboru, který bude obsahovat adresář `du3_jmeno_prijmeni`,
ve kterém bude soubor se zdrojovým kódem a soubor s dokumentací, tedy například:
```
du3.zip
|
\du3_tomas_pokorny
  |- README.md
  \- du3.py
```
Zip archiv mi pošlete mailem. 

Deadline na odevzdání je týden před tím, než chcete mít udělen zápočet. Pokud se
ukáže, že dané vypracování na zápočet nestačí, můžete pokračovat v úpravách a
zkusit ho odevzdat znovu.
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

## Bonusové body

### Používání Gitu pro vývoj s vhodnými popisy commitů (1 b)
Pokud budete pro verzování používat Git, vytvořte si účet na GitHubu nebo jiné
podobné stránce a úkol můžete odevzdat přes něj. Kromě samotného odevzdání je
třeba, aby byl repozitář používán i pro vývoj, tedy by měl obsahovat průběžně
commitovanou práci a jednotlivé commity by měly obsahovat stručný a jasný popis
toho, co se v daném commitu změnilo. Repozitář by měl obsahovat jak program, tak
případný soubor s dokumentací, za hodnocenou verzi se počítá poslední commit
pushnutý na GitHub před deadlinem. Repozitář nemusí, ani by neměl, obsahovat
velká vstupní data.  Pokud budete potřebovat pomoct, pište mi.

### Další bonusy
Pokud byste potřebovali dohnat body pomocí dalších bonusů, ozvěte se a domluvíme
se.

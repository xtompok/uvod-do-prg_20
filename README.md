# Úvod do programování (2020 edition)
Zdrojové kódy a poznámky ke cvičení z Úvodu do programování.

[Stránky](http://web.natur.cuni.cz/~bayertom/index.php/9-teaching/10-uvod-do-programovani) přednášky.

Věci probírané na jednotlivých cvičeních najdete na [samostatné stránce](prubeh.md).
Cvičení probíhá rámcově podle kurzu [Nauč se Python!](https://naucse.python.cz/course/pyladies/).
[Dokumentace](https://docs.python.org/3/) k Pythonu 3.

Cvičení probíhá v jazyku Python 3. Možná jste se setkali, například na Programování pro GIS, s Pythonem 2, pak pozor, jazyky jsou podobné, ale ne stejné, například `print` v Pythonu 3 se vždy volá se závorkami.

## Požadavky na zápočet
Celkem budou zadány 3 domácí úkoly po 10 bodech, na zápočet je třeba získat alespoň 23 bodů. Každý domácí úkol bude mít i bonusové části, za které je možné získat body navíc. 

Účast na cvičení je dobrovolná, ale v případě přetlaku na konzultace budou mít přednost ti, kteří se cvičení účastní. 

[Bodování úkolů](./vysledky.md)

## Programové vybavení
### Interpret Pythonu
Ať už budeme používat jakékoli vývojové prostředí, je potřeba si nanistalovat interpret Pythonu 3 - program, který vezme váš zdrojový kód, přeloží ho do instrukcí srozumitelných vašemu počítači a postupně ho provádí. Interpret stáhnete například ze [stránek Pythonu](https://www.python.org/downloads/windows/)(zde `Latest Python 3 Release` a tam dole `Windows x86-64 executable installer`). Pokud používáte Linux nebo Mac OS a nevíte si rady, napište mi prosím. Při instalaci pak na úplně první obrazovce dole zaškrtněte `Add Python 3.8 to PATH`, což vám následně umožní Python snadno spouštět.
![instalator](https://docs.python.org/3/_images/win_installer.png)

### Vývojové prostředí
Vývojové prostředí je program, který nám umožní jednoduše editovat a spouštět zdrojové kódy a dívat se, co naše programy dělají. Jedno vývojové prostředí může být určeno pro více jazyků (Visual Studio Code), nebo jen pro jeden (PyCharm).

Na cvičení budeme programovat v Pythonu 3 v prostředí [Visual Studio Code](https://docs.python.org/3/_images/win_installer.png)(dále VSCode), stáhněte si ho a následně si ho nastavte pro Python dle [návodu](https://code.visualstudio.com/docs/languages/python). Pro nastavení je potřeba již mít nainstalovaný Python 3. Pro konzultace a rady bude používán [Visual Studio Code Live Share](https://visualstudio.microsoft.com/cs/services/live-share/), doporučuji si tedy nainstalovat [Live Share Extension Pack](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare-pack), lze to přímo z VSCode kliknutím na kostičky v levém sloupci. 

Další vhodné prostředí pro Python je [PyCharm](https://www.jetbrains.com/pycharm/), můžete si stáhnout zdarma dostupnou Community Edition. Můžete samozřejmě použít i jiná prostředí, pokud jsou vám bližší.

Pokud si potřebujete jen něco menšího vyzkoušet, tak není potřeba instalovat Python a vývojové prostředí, ale můžete si to vyzkoušet online na [repl.it](https://repl.it/). Když si zkopírujete adresu, co vám to přidělí a někomu ji pošlete, tak můžete společně vyvíjet, všichni, kdo mají otevřenou danou adresu vidí aktuální kód a mohou do něj zasahovat. 

### Komunikace
Pro cvičení budeme využívat [MS Teams](https://www.microsoft.com/cs-cz/microsoft-365/microsoft-teams/group-chat-software), měli byste mít přístup přes [fakultní přihlášení](https://www.natur.cuni.cz/fakulta/aktuality/teams-navod), případně lze do přihlašovacího okna zadat `a@cuni.cz` a přihlásit se přes CAS, kam vás to přesměruje. Detaily dořešíme na prvním cvičení. 

## Tipy a rady pro čitelný kód
### Magické konstanty
Pokud ve svém kódu používáte nějaké konstanty, ať už matematické (např. pi),
fyzikální nebo jste si jen pevně zvolili délku seznamu či např. rozestup
rovnoběžek, je vhodné tyto konstanty na začátku programu pojmenovat a pak
používat toto pojmenování místo jejich číselné hodnoty. Je pak jasné, co je v
daném místě sémanticky myšleno a pokud se nějakou z konstant později rozhodntete
změnit, lze to udělat snadno na jednom dobře definovaném místě.

Konstanty se obvykle pojmenovávají velkými písmeny, víceslovné se oddělují
podtržítkem. Např. `LIST_LEN` pro délku seznamu (pokud v programu je více
seznamů různých délek, je vhodné přidat do jména jednoznačný identifikátor, ke
kterému seznamu se konstanta vztahuje), `F_G = 9.81` pro gravitační zrychlení na
Zemi, `REC_DEPTH` pro hloubku rekurze. Pokud konstantu importujete z nějakého
modulu, nechte ji takové jméno, jaké má v daném modulu (např. `from math import
pi)`.

### Funkce
Funkce by měly používat pouze lokální proměnné, tedy takové proměnné, jaké buď
dostaly jako argumenty, nebo byly v dané funkci vytvořeny. V opačném případě,
pokud použijete funkci jinde, než bylo původně zamýšleno, může dojít k pádu
aplikace nebo neočekávanému chování, protože některé proměnné nemusí existovat.

Funkce je vhodné psát na začátek souboru za importy a definice konstant. Hlavní
kód by pak měl být na konci souboru pod všemi funkcemi, aby se s nimi nemíchal a
tím pádem nebyla některá jeho část snadno přehlédnutelná. Pokud je v programu
více funkcí vztahujících se k podobnému tématu, je vhodné je oddělit do
samostatného modulu. Usnadní to pak jejich znovupoužitelnost v dalších
programech.

### Nejprve validuj, pak počítej
Pokud program bere nějaká data od uživatele, ať už přímo přes `input`, pomocí
parametrů příkazové řádky nebo načítá ze souboru, je vhodné (pro některé
aplikace, například webové i nutné) takováto data kontrolovat, zda mají správný
formát a obsah. Tyto kontroly je vhodné provést co nejdříve a až po kontrole
všech vstupních dat s nimi zahájit výpočet.

Tento postup má několik výhod:
 * Uživatel se dozví hned při spuštění, že data nejsou validní a má možnost data
   opravit a program spustit znovu. Pokud se po problému dozví po několika
   hodinách výpočtu, bude jeho práce výrazně méně efektivní
 * Výpočetní funkce již nemusí znovu ověřovat validitu dat, mohou se soustředit
   na samotný výpočet a vstup předpokládat validní. Pokud dojde v rámci úprav
   kódu k přehození pořadí výpočtů, nehrozí při tom práce s nezkontrolovanými
   daty.

Na časté kontroly je vhodné si napsat samostatné funkce, například funkci
`input_int(quest)`, která vypíše `quest` - otázku, kterou se ptáme uživatele,
načte, co uživatel napsal a zkusí to převést na `int` a podle výsledku buď vrátí
číslo, nebo se zeptá znovu. Obdobně lze vytvořit další pomocné funkce, které
povedou k výraznému zjednodušení získávání dat od uživatele.

## Dokumentace
Každý program by měl obsahovat alespoň základní uživatelskou dokumentaci,
rozsáhlejší programy pak i dokumentaci programátorskou.

### Uživatelská dokumentace
Představte si, že kamarádovi vysvětlujete, jak se ten program používá. Kamarád
se rámcově orientuje v tématu programu (tedy např. ví, co jsou to válcová
zobrazení), ale programovat neumí a chce jen program používat, tedy je vhodné
mu říct, jak má co kam zadat, co se případně stane, když něco zadá špatně a co
se vypíše a jak to má použít.

### Vývojářská dokumentace
Pokud je program rozsáhlejší, píše se i programátorská dokumentace,
tedy máte jiného kamaráda, který se opět rámcově orientuje v tématu
programu, ale navíc umí programovat. Zdroják vašeho programu ale nikdy
neviděl. Tato část dokumentace by tedy měla obsahovat stručný popis
běhu programu a stručný popis složitějších funkcí. Také by měla
popisovat použité algoritmy. Doplňkem této dokumentace jsou docstringy
u jednotlivých funkcí, které říkají vstupní a výstupní parametry každé
funkce.


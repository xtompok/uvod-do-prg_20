# Poznámky ze 4. cvičení
## Příkazová řádka:
 - `cd` - změna adresáře
 - `ls` (na windows `dir`) - obsah adresáře
 - `ls -a` (na win `dir /a`) - obsah adresáře včetně skrytých souborů

## Git
 - [https://naucse.python.cz/course/pyladies/git/basics/](https://naucse.python.cz/course/pyladies/git/basics/)
 - `git status` - aktuální stav repozitáře

## Vim
Ukončení bez uložení: `Escape`,`dvojtečka`,`q`,`vykřičník`,`enter`

## Řetězce:
 - `a[3]` - třetí znak řetězce (počítáme od 0)
 - `a[-2]` - předposlední znak
 - `a[3:5]` - třetí a čtvrtý znak (pravá mez tam již nepatří)
 - `a[:5]` - od začátku po pátý znak, ten již ne
 - `a[3:]` - od třetího znaku včetně do konce
 - `a[1:-1]` - řetězec bez prvního a posledního znaku

## Příklady
### Příklad 1:
 - Vytvořte nový repozitář (`git init` ve složce, kterou chcete verzovat)
 - Přidejte do něj nějaký soubor (`git add <soubor>`)
 - Udělejte první commit (`git commit`)

### Příklad 2:
Napište převodník z formátu DMS na stupně, když víte, že DMS bude mít formát `Ndd mm' ss.sss"` (Např. N49 12' 34.235"). Program se na začátku na tento řetězec zeptá uživatele, převede ho a zobrazí výsledek ve stupních.

# Poznámky z 10. cvičení

## Slovníky
  - klíč musí být neměnný
      - int, str, boolean, tuple
  - `klic in slovnik` vrací True, pokud `slovnik` obsahuje klíč `klic`
## Modul `json`
  - načítání ze souboru: `json.load`
  - načítaní z řetězce: `json.loads`
  - zapisování do souboru: `json.dump`
  - zapisování do řetězce: `json.dumps`
  - vhodné parametry pro zápis
    - `ensure_ascii=False` - řetězce s háčky a čárkami budou vypadat normálně a nebudou v nich sekvence se zpětným lomítkem
    - `indent=2` - soubor bude dobře čitelný i pro člověka, nejen pro program

## Data online v JSONu
  - https://mapa.pid.cz/
    - https://mapa.pid.cz/getData.php
    - `delay` je zpoždění v sekundách
    - `route` je číslo linky
  - https://www.pocasi-kucerov.cz/index.php
    - https://www.pocasi-kucerov.cz/weewx/gauge-data.txt

## Requests
  - `pip install requests`
  - pokud máte problémy na Windows, zkuste spustit `C:/Users/<uzivatel>/AppData/Local/Programs/Python/Python37/python.exe -m pip install requests`

## Příklad 0
Pokračujte v [TicTacToe z minula](https://github.com/xtompok/uvod-do-prg_20/tree/master/cv09#p%C5%99%C3%ADklad-1), tedy upravte TicTacToe tak, aby nebylo možné táhnout na pole, kde již je nějaký symbol

## Příklad 1
Zjistěte aktuální průměrné zpoždění autobusů v PID

## Příklad 2
Zjistěte celkové zpoždení autobusů pro jednotlivé linky

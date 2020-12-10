import requests

# Stáhneme aktuální data o zpoždění
resp = requests.get("https://mapa.pid.cz/getData.php")

data = resp.json()
#print(type(data))
#print(data.keys())
trips = list(data['trips'].values())
#print(trips[0])

routes = {}

# trip reprezentuje jeden spoj (jedno vozidlo)
for trip in trips:
    r = trip['route'] # route obsahuje označení linky
    delay = trip['delay'] # delay obsahuje zpoždění (v sekundách)

    # Pokud je již linka aktuálního spoje ve slovníku
    if r in routes:
        # Přičteme zpoždění spoje k celkovému zpoždění linky
        routes[r]['sumdelay'] += delay
        #routes[r]['sumdelay']= routes[r]['sumdelay'] + delay
        # Zvýšíme počet spojů linky o 1
        routes[r]['count'] += 1
    # Pokud linku aktuálního spoje ve slovníku nemáme
    else:
        # Přidáme linku do slovníku
        #   - celkové zpoždění odpovídá zpoždění aktuálního spoje
        #   - toto je první spoj dané linky, tedy počet spojů nastavíme na 1
        routes[r] = {'sumdelay':delay, 'count':1}

# Projdeme slovník všech linek a pro každou vypočteme a zobrazíme průměrné zpoždění
for route, delays in routes.items():
    avg = delays['sumdelay']/delays['count']
    print(f"Linka {route} má průměrné zpoždění {avg}")

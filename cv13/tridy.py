print(type('ahoj'))
print('ahoj'.upper())
print('cau'.upper())
print(int('10'))

# Třída říká, jaké metody budou mít všechny objekty z ní vytvořené

class Trida:
    data2 = 2

    # Inicializator objektu, zde mu muzeme nastavit atributy
    def __init__(self,data=0):
        self.data = data
        self.atr2 = None
    
    # Bezna metoda objektu
    def moje_metoda(self):
        print("data: ",self.data)
	print("data2: ",self.data2)

# Vytvoreni objektu tridy Trida
objekt = Trida()
# Zavolani metody objektu
objekt.moje_metoda()
# Zmena atributu objektu
objekt.data = 24
objekt.moje_metoda()

# POZOR! Tento prikaz vytvori atribut `data2` objektu `objekt`, ktery prekryje
# atribut `data2` tridy `Trida`. 
objekt.data2 = 44

# Pokud chceme modifikovat atribut tridy `Trida`, musime pouzit nasledujici konstrukci
Trida.data2 = 24

# Vice o atributech tridy a objektu na https://dzone.com/articles/python-class-attributes-vs-instance-attributes


# Vytvoreni jineho objektu tridy Trida
obj2 = Trida()
obj2.data = 42
obj2.moje_metoda()
objekt.moje_metoda()

# `objekt` ma vlastni atribut `data2`
print(objekt.data2)
# `obj2` nema vlastni atribut `data2`, pouzije tedy atribut tridy
print(obj2.data2)
# `Trida` take pouzije svuj atribut (atribut tridy)
print(Trida.data2)

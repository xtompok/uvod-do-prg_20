from pyproj import CRS, Transformer

# Vytvoříme objekty souřadnicových systémů
crs_wgs = CRS.from_epsg(4326) # WGS-84
crs_jtsk = CRS.from_epsg(5514) # S-JTSK

# Vytvoříme transformační objekt (stačí jednou pro všechny převody)
wgs2jtsk = Transformer.from_crs(crs_wgs,crs_jtsk)

# Převedeme souřadnice z jednoho systému do druhého (vrací dvojici souřadnic)
jtsk = wgs2jtsk.transform(50,15) # Nejprve sirka, pak delka

# Objekt pro opačný směr
jtsk2wgs = Transformer.from_crs(crs_jtsk,crs_wgs)

# Hvězdička "rozbalí" ntici
print(jtsk2wgs.transform(*jtsk))

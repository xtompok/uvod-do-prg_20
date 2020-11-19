"""
1) načtu ze souboru mesta.txt do seznamu názvy měst
  - nezapomenu oříznout bílé znaky
2) ze seznamu vyberu náhodné město
3) Vyrobím seznam `uhadnuto`
  - stejné délky jako hádané město
  - obsahuje samé False
4) Dokud není uhádnuto
    a) Vypíši aktuální stav hádání
      - znaky, jejichž pozice je v seznamu `uhadnuto` True, vypíši
      - místo ostatních napíši podtržítka
    b) Zeptám se uživatele na písmeno
    c) procházím hledané jméno
      - ty pozice v `uhadnuto`, kde se aktuálně hádané písmeno shoduje s písmenem
      ve jméně, přepnu v `uhadnuto` na True
    d) Pokud `uhadnuto` obsahuje jen samé True, tak program skončí."""

choice = input("Pro DMS -> deg zadej dms, pro deg -> DMS zadej deg: ")
enter_coords = "Napiš souřadnici ve formátu {}: "

if choice == "dms":
    formats = "DMS (např. N49 14' 32.234\")"
    dms = input(enter_coords.format(formats))
    out_type = "stupně"

    deg = int(dms[1:3])
    min = int(dms[4:6])
    sec = float(dms[8:-1])

    out_str = "{:.3f}".format(deg+min/60+sec/3600)
else:
    format = "49.12345"
    out_type = "DMS"
    degf = float(input(enter_coords.format(format)))
    deg = int(degf)
    min = int((degf-deg)*60)
    sec = (degf*3600-deg*3600-min*60)
    out_str = f"N{deg} {min}' {sec:.3f}\""

print(f"Převedeno na {out_type} to je {out_str}")
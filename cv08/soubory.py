
f = open('soubor.txt')
print(type(f))
print(f.read())
f.close()

with open('soubor.txt') as f:
    print(f.read())

print("Vypis souboru s cyklem")
with open('soubor.txt') as f:
    for line in f:
        print(line.rstrip())

print("Blok skončil")

with open('soubor_out.txt',mode='w',encoding="windows-1250") as f:
    f.write("ahoj")
    print("Pozdrav z printu",file=f)
    print("Příliš žluťoučký kůň", file=f)

with open('soubor_win.txt', encoding="windows-1250") as infile:
    with open('soubor_utf.txt', encoding="utf-8", mode="w") as outfile:
        outfile.write(infile.read())

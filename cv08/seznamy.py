import random

# vytvoření seznamu
alist = ['a', 12, None, print]
print(alist)

# průchod prvky seznamu
for item in alist:
    print(item)

# k seznamům lze přistupovat jako k řetězcům
print(alist[2])
print(alist[-1])
print(alist[1:-1])
print(type(alist[1:-1]))

# Při přiřazení jednoho seznamu do druhého nedochází ke kopírování prvků,
# ale je zkopírována reference na seznam. Změnou jednoho se tedy změní i druhý.
blist = alist
print('A:',alist)
print('B:', blist)

alist[1] = 42
print('A:', alist)
print('B:', blist)

blist[0] = 'b'

print('A:', alist)
print('B:', blist)

# pokud chceme vytvořit nový seznam se stejnými prvky, můžeme použít
dlist = list(alist)
print(dlist)

# obdobně můžeme vytvořit seznam z řetězce
strlist = list('ahoj')
print(strlist)


# přidávání do seznamu
alist.append('ahoj')
print('A:', alist)
alist.extend([1,2,3])
print('A:', alist)

# odebírání ze seznamu
print(alist.pop())
print('A:', alist)

alist.remove(1)
print('A:', alist)

# vyčištění seznamu
alist.clear()
print('A:', alist)

# hledání prvků v seznamu
clist = [1,2,3,3,4]
print(len(clist))
print(clist.count(3))
print(clist.index(3))

# seznamy a náhoda
random.shuffle(clist)
print(clist)

print(random.choice(clist))
print(clist)

# kontrola přítomnosti prvku v seznamu
'a' in 'ahoj'
print(1 in clist)

# řazení seznamu
cisla = [1,7,3,4,9]
print(cisla)
cisla.sort(reverse=True)
print(cisla)

# aritmetika se seznamy
elist = [1,2,3]+[4,5,6]*3
print(elist)

#kontrola prázdného seznamu
if len(elist) == 0:
    print("Prázdný seznam")

if elist:
    print("Neprázdný")

# rozdělení řetězce na seznam podle daného separátoru
ret = "49 16 34.567"
souradnice = ret.split(" ")
print(souradnice)

# vícerozměrné seznamy (seznamy seznamů)
tabulka = [[1,2,3],[4,5,6],[7,8,9]]
trojuhelnik = [[1],[2,3],[4,5,6]]
radek = tabulka[1]
cislo = radek[-1]
# cislo = tabulka[1][-1]
print(cislo)
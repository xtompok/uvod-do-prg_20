import random

alist = ['a', 12, None, print]
print(alist)

for item in alist:
    print(item)

print(alist[2])
print(alist[-1])
print(alist[1:-1])
print(type(alist[1:-1]))

blist = alist
print('A:',alist)
print('B:', blist)

alist[1] = 42
print('A:', alist)
print('B:', blist)

blist[0] = 'b'

print('A:', alist)
print('B:', blist)

alist.append('ahoj')
print('A:', alist)
alist.extend([1,2,3])
print('A:', alist)

print(alist.pop())
print('A:', alist)

alist.remove(1)
print('A:', alist)

alist.clear()
print('A:', alist)

clist = [1,2,3,3,4]
print(len(clist))
print(clist.count(3))
print(clist.index(3))

random.shuffle(clist)
print(clist)

print(random.choice(clist))
print(clist)

'a' in 'ahoj'
print(1 in clist)

dlist = list('ahoj')
print(dlist)
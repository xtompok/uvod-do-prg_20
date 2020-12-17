def f(n):
    if n == 1:
        return 1
    return n*f(n-1)

print(f(1))
print(f(5))
#print(f(1001))

fac = 1
for i in range(1001):
    fac *= i+1

print(fac)

a = "Ahoj"
b = "Hugo"
c = "Dobrý den"
mystr = "První písmeno z {a} je {a[0]} a řetězec je dlouhý {alen} znaků"
print(mystr)
print(mystr.format(a=a,alen=len(a)))
print(f"První písmeno z {b} je {b[0]} a řetězec je dlouhý {len(b)} znaků")
print("První argument je {} a druhý je {}".format(b,a))
print(f"Pi je přibližně {3.1415927}")
a = 1/17
print("Sedmnáctina je přibližně {:.2f}".format(a))
print(a)


from bitarray import bitarray

a = bitarray([False]*4)
print(a)
a[2] = 1
print(a)
for i in a[True]:
    print(i)
# 11. How can we have two variables refering to a single list, set and dictionary.

l = [1,2,3]
a = l
print(id(a))
print(id(l))

s = {4,5,6}
b = s
print(id(s))
print(id(b))

d = {'a':1,'b':2,'c':3}
f = d
print(id(d))
print(id(f))
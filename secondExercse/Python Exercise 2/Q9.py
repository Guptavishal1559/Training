# 9. Two dictionaries {'a':1,'b':2,'c':3}, {'a':4,'d':5,'e':6}. Merge these two dictionaries.

a = {'a':1,'b':2,'c':3}
b = {'a':4,'d':5,'e':6}

print(a)
print(b)

a.update(b)

print(a)
# 18. Create a function that will take unlimited arguments and should add all the
# arguments which are passed.

def unlimited(*args):
    add = 0
    for i in args:
        add += i
    return add




print(unlimited(10,20,30))
print(unlimited(20,30,50))
print(unlimited(10,30,50))
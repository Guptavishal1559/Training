# 23. Create a two funcitons. Call one function from another function.

def A():
    a = 4
    b = 6
    print(a + b)

def B():
    a = 4
    b = 3
    print(a + b)
    A()

print(B())
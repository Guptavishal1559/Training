# 29. Implement multiple inheritance and multi-level inheritance.


# Multi - Level inheritance
class A:
    print("This is the class A")
class B(A):
    print("This is the class B and its inherit the class A")

class C(B):
    print("This is the class C and its inherit the class B so it will inherit the class A also because it is the multilevel inheritance")

obj = C()


# Multiple inheritance

class D:
    print("This is class D")

class E:
    print("This is the class E")

class F(D,E):
    print("This is the class F and it will inherit the class D and class E and it is the multiple inheritance")


obj1 = F()

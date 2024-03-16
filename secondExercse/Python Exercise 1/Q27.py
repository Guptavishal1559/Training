# 27. Create a constructor and destructor for the above class.

class parent:
    def __init__(self):
        print("This is the constructor method of parent class")

    def method1(self):
        print("I am method 1 from parent class")

    def method2(self):
        print("I am method 2 from parent class")

    def __del__(self):
        print("This is the destructor method of parent class")


class child(parent):

    def __init__(self):
        print("This is the constructor method of child class")

    def method3(self):
        print("I am method 3 from child class")

    def __del__(self):
        print("This is the destructor method of child class")


obj1 = parent()
obj1.method1()
obj1.method2()
# obj1.method3()  ERROR

obj2 = child()
obj2.method1()
obj2.method2()
obj2.method3()

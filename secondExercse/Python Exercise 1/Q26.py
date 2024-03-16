# 26. Create a parent class and a child class. Create two methods in the parent class.
# Create one method in the child class. Create an object of parent and try to access
# the method of parent and child class. Create an object of child class and try to
# access the method of parent and child class.

class parent:
    def method1(self):
        print("I am method 1 from parent class")

    def method2(self):
        print("I am method 2 from parent class")


class child(parent):
    def method3(self):
        print("I am method 3 from child class")



obj1 = parent()
obj1.method1()
obj1.method2()
# obj1.method3()  ERROR

obj2 = child()
obj2.method1()
obj2.method2()
obj2.method3()




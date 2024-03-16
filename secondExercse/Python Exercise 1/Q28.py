# 28. Override and Overwrite a method of the parent class in child class.

class parent:
    def method1(self):
        print("I am method 1 from parent class")


class child(parent):
    def method1(self):
        super().method1()
        print("I am method 1 from child class")

obj = child()
obj.method1()

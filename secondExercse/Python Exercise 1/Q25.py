# 25. Define a class and define two member variables and two methods inside the class.
# One method will have one parameter and other method will not have any
# parameter. Create a constructor for the class accepting two parameters and assign
# them to the class member variables. One of the two methods will perform an
# operation on the member variables and give result. The second method will print
# the result.
class A:
    a = ''
    b = ''

    def __init__(self,fname,lname):
        self.a = fname
        self.b = lname

    def one(self,fullname):
        res = fullname + self.a + self.b
        return res

    def two(self):
        print(self.one("Vishal "))

obj = A("Girijashankar"," Gupta")
obj.two()
# 30. Perform overloading for constructors and methods defined in the class.

class overcons:
    def __init__(self,a=None,b=None):
        if(a != None and b !=None):
            print(a+b)
        elif(a == None and b != None):
            print(b)
        elif(a != None and b == None):
            print(a)
        else:
            print("Nothing")

    def meth(self,a=None,b=None):
        if (a != None and b != None):
            print(a + b)
        elif (a == None and b != None):
            print(b)
        elif (a != None and b == None):
            print(a)
        else:
            print("Nothing")

obj = overcons()
obj = overcons(20)
obj = overcons(10,20)
obj = overcons(b=40)

obj.meth()
obj.meth(20)
obj.meth(20,30)

# 31. Define a class(my_parent_class) with 2 variables x,y and 3 methods. add, sub and
# print_result. Define a child class and override the methods and constructor as
# given below.

# => Parent Class:
# • The methods add,sub will have two params which will be 2 default parameters
# and print_result will not have any params.

# • Create a constructor for this class with 2 default parameters, if the values are
# passed in the object assign those values to the new 2 member variables(a,b)
# else assign the values which are already there in the existing member
# variables(x,y) to new 2 member variables(a,b).

# • Define the methods add and sub which will perform the operation of addition
# and subtraction respectively store the values in two new member variables
# (res1,res2) and call the method print_result. The print_result method will print
# these two member variables(res1,res2).

# • Create three objects, one with no values passed, one with single value passed
# and one with two value passed.

# => Child Class:
# • Inherit the parent class(my_parent_class) in a child class(my_child_class) and
# override the constructor to have an additional parameter which will be again a
# default parameter assigning the value to the child member variable(z).

# • Override add() method which will call the parent class add method using two
# variable but the print_result() method should print the addition of the 3
# member variables(x,y,z) instead of two(x,y) without inheriting the
# print_result() method.

# • Override the sub() method to perform multiplication operation of three member
# variables(x,y,z) instead of subtraction of two member variables(x,y)

# • Override a destructor to show when it is being called automatically and when it
# would be called manually by our code.

# class my_parent_class:
#
#     def __init__(self,a=100,b=200):
#         self. a = a
#         self.b = b
#         self.res1 = None
#         self.res2 = None
#
#     def add(self,a=None,b=None):
#         if  a != None and b != None:
#             self.res1 =  a + b
#         elif a != None :
#             self.res1 = a + a
#         else:
#             self.a = self.a
#             self.b = self.b
#             self.res1 = self.a + self.b
#
#         return self.res1
#
#     def sub(self,c=None,d=None):
#         if  c != None and d != None:
#             self.res1 =  c - d
#         elif c != None :
#             self.res1 = c - c
#         else:
#             self.a = self.a
#             self.b = self.b
#             self.res1 = self.a - self.b
#
#         return self.res1
#
#     def print_result(self):
#         print(self.add())
#         print(self.sub())
#
#
# class my_child_class(my_parent_class):
#     def __init__(self,a,b,z):
#         super().__init__(a,b)
#         self.z = z
#
#     def add(self):
#         super().add()+self.z
#
#     def sub(self):
#         return self.a*self.b*self.z
#
#     def __del__(self):
#         print("This is Destructor method")
#
#
# obj = my_parent_class()
# obj.print_result()
#
# obj_child = my_child_class(10,20,30)
# obj_child.print_result()



class my_parent_class:
    x = 0
    y = 0

    def __init__(self,a=None,b=None):
        if(a != None and b != None):
            self.a = a
            self.b = b
            print(self.a + self.b)

        elif(a != None):
            self.a = a + a
            print(self.a)

        elif(a == None and b == None):
            self.a = self.x
            self.b= self.y
            print(self.a + self.b)

    def add(self,a=None,b=None):
        if (a != None and b != None):
            self.res1 = a + b
            return self.res1

        elif(a != None):
            self.res1 = a + a
            return self.res1

        else:
            self.res1 = "Nothing is passed in the add method"
            return self.res1

    def sub(self,a=None,b=None):
        if (a != None and b != None):
            self.res1 = a - b
            return self.res1

        elif (a != None):
            self.res1 = a - a
            return self.res1

        else:
            self.res1 = "Nothing is passed in the add method"
            return self.res1

    def print_result(self):
        print(self.add())
        print(self.add(20))
        print(self.add(10,20))

        print(self.sub())
        print(self.sub(10))
        print(self.sub(20,30))

class my_child_class(my_parent_class):

    def __init__(self,a,b,z):
        super().__init__(a,b)
        self.z = z

    def add(self,a=None,b=None):
        super().add(a,b)+self.z

    def sub(self):
        return self.a*self.b*self.z

    def __del__(self):
        print("This is Destructor method")






obj_parent = my_parent_class()
obj_parent = my_parent_class(80)
obj_parent = my_parent_class(20,20)
obj_parent.print_result()

obj_child = my_child_class(10,20,30)
obj_child.print_result()
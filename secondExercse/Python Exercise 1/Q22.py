# 22. Create a script/program that will take arguments as 1,2,3,4,5, or 6 and will also
# take operands as arguments based on the selection made it will perform the
# operation and print the result.
# • 1=Addition, 2=Subtraction, 3=Multiplication, 4=Division, 5=Exponent,
# 6=Floor Division. If anything else is passed it should say Invalid argument.
# • Create a parent function which will accept the options and based on the options
# it will call nested functions for each operation. So total 7 functions will be
# created one parent and 6 nested functions.
# • According to the selection made take inputs for the operations. If 1,2,3 are
# selected take 3 inputs as operands and if 4,5,6 are selected take 2 inputs as
# operands. Perform the operation and print the result.


def parent(n):

    def addition(a,b,c):
        return a + b + c

    def subtraction(a,b,c):
        return  a - b - c

    def multiplication(a,b,c):
        return  a * b * c

    def division(a,b):
        if b == 0:
            return "You can't divide by the zero"
        return a / b

    def exponent(a,b):
            return a ** b

    def floor_division(a,b):
        if b == 0:
            return "You can't divied by the zero"
        return a // b


    if n == 1:
        x = int(input("Enter the first Number : "))
        y = int(input("Entefr the second Numeber : "))
        z = int(input("Enter the third Number : "))

        print(addition(x,y,z))

    elif n == 2:
        x = int(input("Enter the first Number : "))
        y = int(input("Entefr the second Numeber : "))
        z = int(input("Enter the third Number : "))

        print(subtraction(x,y,z))

    elif n == 3:
        x = int(input("Enter the first Number : "))
        y = int(input("Entefr the second Numeber : "))
        z = int(input("Enter the third Number : "))

        print(multiplication(x,y,z))

    elif n == 4:
        x = int(input("Enter the first Number : "))
        y = int(input("Entefr the second Numeber : "))

        print(division(x,y))

    elif n == 5:
        x = int(input("Enter the first Number : "))
        y = int(input("Entefr the second Numeber : "))

        print(exponent(x, y))

    elif n == 6:
        x = int(input("Enter the first Number : "))
        y = int(input("Entefr the second Numeber : "))

        print(floor_division(x, y))

    else:
        print("Select the appropriate option....")




z = int(input('''
                Choose Appropriate Number--
                1. Addition
                2. Subtraction
                3. Multiplicatin
                4. Division
                5. Exponent
                6. Floor Division
                '''))

parent(z)

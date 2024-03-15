''' 17. Create a function which will take 4 arguments where 2 wil be mandatory and 2 keyword arguments.
Perform multilpication if 2 values are passed. Perform
addition if 3 are passed.
Perform addition of 1 st two operands and 2nd two operands and then do a subtraction if 4 arguments are passed.'''

def area(a,b,c=None,d=None):
    if(c != None and d != None):
        return (a + b) - (c + d)
    elif(c != None):
        return a + b + c
    elif(c == None and d == None):
        return a * b
    else:
        return "Nothing"

print(area(2,3))
print(area(2,3,4))
print(area(2,3,4,5))


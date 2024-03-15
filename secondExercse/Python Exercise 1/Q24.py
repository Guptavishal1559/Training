# 24. Create a function that will take 5 arguments 2 will be mandatory and 3 will be
# keyword parameters. If 2 parameters are passed perform multiplication of 2
# parameters. If 3 parameters are passed print all the 3 parameters. If 4 parameters
# are passed addition of 4 parameters. If 5 parameters are passed multiply 2 mandatory parameters and then separately multiply 3 keyword parameters and add
# both of them.

def area(a,b,c=None,d=None,e=None):
    if(c == None and d == None and e == None):
        return a * b
    elif(c != None and d == None and e == None):
        return a, b, c
    elif(c != None and d != None and e == None):
        return a + b + c + d
    elif(c != None and d != None and e != None):
        return (a * b) + (c * d * e)

print(area(10,20))
print(area(10,20,c=30))
print(area(10,20,c=30,d=40))
print(area(10,20,c=30,d=40,e=50))
# 20.Write a function with recursion to give the power of a number. It will be having
# two parameters no and power. If no power is passed it should take 0.

def pow(no,power):
    if (power == 0):
        return 1
    elif (power == 1):
        return no
    else:
        return (no * pow (no, power-1))


base = int(input("Enter the base number : "))
power = int(input("Enter the power number : "))

print(pow(base,power))

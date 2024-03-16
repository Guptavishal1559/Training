# 33. Create a function for string that will check whether a string is having the first
# letter as Capital and not anyother letter is capital.

def check_case(name):
    if(name[0].isupper() and name[1::1].islower()):
        return "Okay good your first letter is capital"
    else:
        return "It is not in required format"


name = input("Enter Your Name :- ")
print(check_case(name))

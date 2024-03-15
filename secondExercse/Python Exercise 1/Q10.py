# 10. Create a python script/program that will take input from the user for 3 numbers
# and result will print the biggest number and the smallest number using 'input' and
# 'print'.

#
# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))
# c = int(input("Enter the third number : "))
#
# if (a>b and a>c):
#     print(f"TThe Biggest Number is : {a}")
#     if b < c:
#         print(f"Smallest number is {b}")
#     else:
#         print(f"Smallest number is {c}")
# elif (b>a and b>c):
#     print(f"The Biggest Number is : {b}")
#     if a < c:
#         print(f"Smallest number is {a}")
#     else:
#         print(f"Smallest number is {c}")
# else:
#     print(f"The Biggest Number is : {c}")
#     if a < b:
#         print(f"Smallest number is {a}")
#     else:
#         print(f"Smallest number is {a}")


a=list(map(int,(input("Enter three number separated by commas : ").split(","))))
print(a,type(a))
max = max(a)
min = min(a)
print(f"Maximum number is {max} and Minimum number is {min}")
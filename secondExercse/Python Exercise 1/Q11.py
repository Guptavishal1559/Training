# 11. Create another script/program using 'input' and pass all the three parameters as a
# single input and execute the same program as mentioned above.

x,y,z= map(float,input("Enter any three number separated by comma :").split(","))
max_number = max(x,y,z)
min_number = min(x,y,z)
print(f"The Biggest Number is {max_number}")
print(f"The Smallest Number is {min_number}")
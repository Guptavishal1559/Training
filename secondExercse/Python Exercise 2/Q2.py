# 2. Get a list of 1 to 20 then remove elements from list to get only even elements.

num = [num for num in range(1,21)]
print(num)
even_number = [numbers for numbers in num if numbers % 2 == 0]
print(even_number)
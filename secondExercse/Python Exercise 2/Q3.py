# 3. Get a list of 1 to 8 and then 4 to 10. Get the common elements from both the list in
# a new list.

# l1 = [1,2,3,4,5,6,7,8]
# l2 = [4,5,6,7,8,9,10]
l1 = [l1 for l1 in range(1,9)]
l2 = [l2 for l2 in range(4,11)]

new_list = set(l1).intersection(l2)
print(list(new_list))
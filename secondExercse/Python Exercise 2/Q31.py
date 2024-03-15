# 31. There are two lists [1,2,3,4,5], [4,5,6,7] get a list from these two lists [1,2,3,6,7].

l1 = [1,2,3,4,5]
l2 = [4,5,6,7]


l = list(set(l1 + l2))
print(l)


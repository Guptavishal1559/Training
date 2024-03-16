# 29. There are two lists [1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]. Get a
# third list from these two lists as [12,14,16,18,20,22,24,26,28,30].


l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [11,12,13,14,15,16,17,18,19,20]

# l = []
# for i in range(len(l1)):
#     l.append(l1[i] + l2[i])
# print(l)

l = list(map(lambda x,y:x+y, l1,l2))
print(l)
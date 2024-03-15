# 7. Generate a dictionary {1:1,2:1,3:1,4:1,...,10:1} in one line using dictionary's method.

d = dict.fromkeys(range(1,11),1)
print(d)
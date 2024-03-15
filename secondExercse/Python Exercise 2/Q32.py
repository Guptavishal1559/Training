# 32. Fetch the data from the following.

# 1. Fetch 5 which is the value of ‘e’ from below which is marked in red.
x = {'a':1, 'b':2, 'c':3,'d':[1,2,3,4,(5,6,7,{'e':5})]}
print(x['d'][4][3]['e'])

# 2. Fetch 2 from below which is marked in red.
x = {'a':{'b':[1,2,(3,4,{'c':3,'d':4,'e':[1,2,3]})]}}
print(x['a']['b'][2][2]['e'][1])

# 3. Fetch 6 from below which is marked in red.
x = [1, 2, (3, 4, 5, {'a':1, 'b':[2,3,4,(5,6)]})]
print(x[2][3]['b'][3][1])

# 4. Fetch 2 from above which is marked in red.
x = {True:[1,2,3,{'a':1,'b':2}],False:[(2,3,4,5,{1:2})]}
print(x[0][0][4][1])

# 5. Fetch 9 from above which is marked in red.
x = {1:2,2:3,3:4,4:{'a':'b','c':'d','e':'f','f':[1,2,3,{1:9,3:8}]}}
print(x[4]['f'][3][1])


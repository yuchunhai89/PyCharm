__author__ = 'yuchunhai'
#== 和 is的差别，==比较的是值，is比较的是引用。
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x == y) #True
print(x == z) #True
print(x is y) #True
print(x is z) #False
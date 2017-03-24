# __author__ = 'yuchunhai'
# 1、for循环依次把list或tuple的每个元素迭代出来
# 格式
# for 元素 in 序列:
#     statement
# name 这个变量是在 for 循环中定义的，意思是，依次取出list中的每一个元素，并把元素赋值给 name，然后执行for循环体（就是缩进的代码块）
# L = ['Adam', 'Lisa', 'Bart']
# for name in L:
#     print name
# 这样一来，遍历一个list或tuple就非常容易了。
#  2、while循环，不会迭代 list 或 tuple 的元素，而是根据表达式判断循环是否结束。
# while 条件:
#     statement
# 3、中断循环 break和continue
# 4、range()的用法
# range(1,5) #代表从1到5(不包含5)   [1, 2, 3, 4]
# range(1,5,2) #代表从1到5，间隔2(不包含5)   [1, 3]
# range(5) #代表从0到5(不包含5)   [0, 1, 2, 3, 4]
# 5、Python中，迭代永远是取出元素本身，而非元素的索引。
# 对于有序集合，元素确实是有索引的。使用enumerate() 函数拿到索引
# 复制代码
# L = ['Adam', 'Lisa', 'Bart', 'Paul']
# for index, name in enumerate(L):
#     print index, '-', name
# #结果
# # 0 - Adam
# # 1 - Lisa
# # 2 - Bart
# # 3 - Paul
# 复制代码
# 使用 enumerate() 函数，我们可以在for循环中同时绑定索引index和元素name。但是，这不是 enumerate() 的特殊语法。实际上，enumerate() 函数把：
# ['Adam', 'Lisa', 'Bart', 'Paul']
# 变成了类似：
# [(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]
# 因此，迭代的每一个元素实际上是一个tuple：
# 6、好用的zip()方法
# 复制代码
# for x, y in zip(range(1, 10), range(1, 10)):
#     print(x, y)
# # 结果
# # (1, 1)
# # (2, 2)
# # (3, 3)
# # (4, 4)
# # (5, 5)
# # (6, 6)
# # (7, 7)
# # (8, 8)
# # (9, 9)
# 复制代码
# 7、列表生成式，非常简洁
# 要生成[1x1, 2x2, 3x3, ..., 10x10]
# print [x * x for x in range(1, 11)]
# #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 列表生成式的 for 循环后面还可以加上 if 判断。例如：
# print  [x * x for x in range(1, 11) if x % 2 == 0]
# # [4, 16, 36, 64, 100]
# 8、迭代器
# 它为类序列对象提供了一个类序列的接口。
# 迭代非序列集合(例如映射和文件)时, 可以创建更简洁可读的代码。
# myTuple = (123, 'xyz', 45.67)
# i = iter(myTuple)
# print i.next()  #123
# print i.next()  #xyz
# print i.next()  #45.67
# i.next()        #报错
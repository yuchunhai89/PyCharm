# __author__ = 'yuchunhai'
# 1、由于参数 x, y和 f 都可以任意传入，如果 f 传入其他函数，就可以得到不同的返回值。
#
# def add(x, y, f):
#     return f(x) + f(y)
# print add(-5, 9, abs)  #abs(-5) + abs(9) = 14
# 2、map() 映射
#
# map()是 Python 内置的高阶函数，它接收一个函数f和一个list，并通过把函数f依次作用在 list的每个元素上，得到一个新的 list 并返回。
#
# def f(x):
#     return x*x
# print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])  #[1, 4, 9, 16, 25, 36, 49, 64, 81]
# 利用map()函数，可以把一个 list 转换为另一个 list，只需要传入转换函数。
#
# 由于list包含的元素可以是任何类型，因此，map()不仅仅可以处理只包含数值的 list，事实上它可以处理包含任意类型的 list，只要传入的函数f可以处理这种数据类型。
#
# 3、reduce()折叠
#
# reduce()函数接收的参数和 map()类似，一个函数f，一个list，但reduce()传入的函数f必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。
#
# 复制代码
# def f(x, y):
#     return x + y
# print reduce(f, [1, 3, 5, 7, 9])  #25
# #先计算头两个元素：f(1, 3)，结果为4；
# #再把结果和第3个元素计算：f(4, 5)，结果为9；
# #再把结果和第4个元素计算：f(9, 7)，结果为16；
# #再把结果和第5个元素计算：f(16, 9)，结果为25；
# #由于没有更多的元素了，计算结束，返回结果25。
# #初始值100
# print reduce(f, [1, 3, 5, 7, 9], 100)   #125
# 复制代码
# reduce()还可以接收第3个可选参数，作为计算的初始值。
#
# 4、filter() 过滤
#
# filter()函数接收一个函数f和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。
#
# def is_odd(x): #是奇数
#     return x % 2 == 1
# print filter(is_odd, [1, 4, 6, 7, 9, 12, 17])   #[1, 7, 9, 17]
# 利用filter()，可以完成很多有用的功能，例如，删除 None 或者空字符串：
#
# def is_not_empty(s):
#     return s and len(s.strip()) > 0
# print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
# #['test', 'str', 'END']
# 5、sorted()：对list进行排序
#
# print sorted([36, 5, 12, 9, 21])  #[5, 9, 12, 21, 36]
# 但sorted()也是一个高阶函数，它可以接收一个比较函数来实现自定义排序，比较函数的定义是，传入两个待比较的元素x, y，如果x应该排在y的前面，返回-1，如果x应该排在y的后面，返回1。如果x和y相等，返回0。
#
# 复制代码
# #倒序排序
# def reversed_cmp(x, y):
#     if x > y:
#         return -1
#     if x < y:
#         return 1
#     return 0
# print sorted([36, 5, 12, 9, 21], reversed_cmp)  #[36, 21, 12, 9, 5]
# 复制代码
# 6、Python的函数不但可以返回int、str、list、dict等数据类型，还可以返回函数！
#
# 复制代码
# def f():
#     print 'call f()...'
#     # 定义函数g:
#     def g():
#         print 'call g()...'
#     # 返回函数g:
#     return g
#
# x = f()  # 调用f()  call f()...
# x   # 变量x是f()返回的函数：  #<function g at 0x00000000022CDA58>
# x()  # x指向函数，因此可以调用  call g()...
# x=f(),x()=g()
# 复制代码
# 请注意区分返回函数和返回值：
#
# def myabs():
#     return abs   # 返回函数
# def myabs2(x):
#     return abs(x)   # 返回函数调用的结果，返回值是一个数值
# 在函数内部定义的函数和外部定义的函数是一样的，只是他们无法被外部访问：
#
# 7、闭包（closure）
#
# 内部函数中引用了外层函数的变量（enclosing作用域的变量），然后返回内层函数的情况。
#
# 闭包的作用是封装和代码复用。
#
# 传递的是参数
#
# 复制代码
# #如果要实现两个功能，可以定义两个函数。
# def func_150(val):
#     passline = 90  #150
#     if val >= passline:
#         print ("pass")
#     else:
#         print "failed"
#
# def func_100(val):
#     passline = 60  #150
#     if val >= passline:
#         print ("pass")
#     else:
#         print "failed"
#
# func_100(69)#pass
# func_150(69)#failed
#
# #如果用闭包的话只需要定义一个函数
# def set_passline(passline):#passline
#     def cmp(val):
#         if val >= passline:
#             print "pass"
#         else:
#             print "failed"
#     return cmp  #返回值是一个函数
#
# f_100 = set_passline(60) #f_100就是cmp,f_100()就是cmp()，而且内置一个passline=60
# f_150 = set_passline(90)
#
# f_100(69)#pass
# f_150(69)#failed
# 复制代码
# 传递的是函数
#
# 复制代码
# #不用闭包
# def my_sum(*arg):
#     if len(arg)==0:
#         return 0
#     for val in arg:
#         if not isinstance(val,int):
#             return 0
#     return sum(arg)
#
# def my_average(*arg):
#     if len(arg)==0:
#         return 0
#     for val in arg:
#         if not isinstance(val,int):
#             return 0
#     return sum(arg)/len(arg)
#
# print my_sum(1,2,3,4,5) #15
# print my_sum(1,2,3,4,5,'6')#0
# print my_average(1,2,3,4,5)#3
# print my_average()#0
#
# #使用闭包
# def my_sum(*arg):
#     print "in my_sum"
#     return sum(arg)
#
# def my_average(*arg):
#     return sum(arg)/len(arg)
#
# def dec(func):
#     def in_dec(*arg):
#         print "in_dec()=",arg
#         if len(arg) == 0:
#             return 0
#         for val in arg:
#             if not isinstance(val, int):
#                 return 0
#         return func(*arg)
#     return in_dec  #别加括号
# #dec return in_dec -> my_sum
# #my_sum = in_dec(*arg)
# my_sum = dec(my_sum)
# my_average = dec(my_average)#同理
#
#
# print my_sum(1,2,3,4,5)
# print my_sum(1,2,3,4,5,'6')
#
# # 结果
# # in_dec()= (1, 2, 3, 4, 5)
# # in my_sum
# # 15
# # in_dec()= (1, 2, 3, 4, 5, '6')
# # 0
# 复制代码
# 正确使用闭包，就要确保引用的局部变量在函数返回后不能变。
#
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量。
#
# 复制代码
# # 希望一次返回3个函数，分别计算1x1,2x2,3x3:
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
# f1, f2, f3 = count()
# print f1(),f2(),f3()  #9 9 9
# #当count()函数返回了3个函数时，这3个函数所引用的变量 i 的值已经变成了3。由于f1、f2、f3并没有被调用，所以，此时他们并未计算 i*i，当 f1 被调用时，才计算i*i，但现在i的值已经变为3
#
# #正确如下
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f(j):
#             def g():
#                 return j*j
#             return g
#         r = f(i)
#         fs.append(r)
#     return fs
# f1, f2, f3 = count()
# print f1(), f2(), f3()  #1 4 9
# 复制代码
# 8、匿名函数lambda
#
# def f(x):
#     return x*x
# print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])  #[1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]) #[1, 4, 9, 16, 25, 36, 49, 64, 81]
# 通过对比可以看出，匿名函数 lambda x: x * x 实际上就是：
#
# def f(x):
#
#     return x * x
#
# 关键字lambda表示匿名函数，冒号前面的x 表示函数参数。
#
# 匿名函数有个限制，就是只能有一个表达式，不写return，返回值就是该表达式的结果。
#
# 使用匿名函数，可以不必定义函数名，直接创建一个函数对象，很多时候可以简化代码：
#
# print sorted([1, 3, 9, 5, 0], lambda x,y: -cmp(x,y))  #[9, 5, 3, 1, 0]
# 返回函数的时候，也可以返回匿名函数：
#
# myabs = lambda x: -x if x < 0 else x
# print myabs(-1)  #1
# print myabs(1)   #1
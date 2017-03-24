# __author__ = 'yuchunhai'
# 1、定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用 return 语句返回。
# def say_b():
#     print "b"
# say_b()  #调用函数，打印出b
# 2、如果没有return语句，函数执行完毕后也会返回结果，只是结果为 None。
# 3、函数返回多个值
# 复制代码
# import math
# def move(x, y, step, angle):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# x, y = move(100, 100, 60, math.pi / 6)
# print x, y   #151.961524227 70.0
# r = move(100, 100, 60, math.pi / 6)
# print r    #(151.96152422706632, 70.0)
# 复制代码
# 其实这只是一种假象，Python函数返回的仍然是单一值，是一个tuple：
# 但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
# 4、在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
# print fact(10)  #计算10的阶乘
# 5、定义函数的时候，还可以有默认参数。
# 复制代码
# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print power(2)  #默认计算2的平方
# print power(2,3)  #计算2的三次方
# 复制代码
# 由于函数的参数按从左到右的顺序匹配，所以默认参数只能定义在必需参数的后面：
# 6、一个函数能接受任意个参数，我们就可以定义一个可变参数：
# def fn(*args):
#     print args
# fn('a')   #('a',)
# fn('a', 'b')  #('a', 'b')
# fn('a', 'b', 'c')   #('a', 'b', 'c')
# 可变参数的名字前面有个 * 号，我们可以传入0个、1个或多个参数给可变参数：
# 7、基本数据类型的参数：值传递
# 表作为参数：指针传递
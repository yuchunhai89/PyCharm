# __author__ = 'yuchunhai'
# 1、decorator本质上就是一个高阶函数，它接收一个函数作为参数，然后，返回一个新函数。
#
# 使用 decorator 用Python提供的@语法，这样可以避免手动编写f=decorate(f)这样的代码。
#
# 2、装饰器用来装饰函数，返回一个函数对象
#
# 被装饰函数标识符指向返回的函数对象
#
# 复制代码
# def dec(func):
#     print "call dec"
#     def in_dec(*arg):
#         print "in_dec()=",arg
#         if len(arg) == 0:
#             return 0
#         for val in arg:
#             if not isinstance(val, int):
#                 return 0
#         return func(*arg)
#     return in_dec  #别加括号
#
# @dec    # 代替了my_sum = dec(my_sum)
# def my_sum(*arg): #my_sum = in_dec
#     print "in my_sum"
#     return sum(arg)
#
# print my_sum(1,2,3,4,5)
#
# # call dec
# # in_dec()= (1, 2, 3, 4, 5)
# # in my_sum
# # 15
# 复制代码
# 3、传入函数，含有两个参数
#
# 复制代码
# def deco(func):
#     def in_deco(x,y):
#         print "in deco"
#         func(x,y)
#     print "call deco"
#     return in_deco
#
# @deco  #代替 bar = deco(bar) = in_deco    #bar()-> in_deco()->bar()
# def bar(x,y):
#     print "in bar",x+y
#
# bar(1,2)
#
# # call deco
# # in deco
# # in bar
# 复制代码
# 4、@log的定义
#
# 复制代码
# def log(f):
#     def fn(x):
#         print 'call ' + f.__name__ + '()...'
#         return f(x)
#     return fn
#
# @log
# def factorial(n):
#     return reduce(lambda x,y: x*y, range(1, n+1))
# print factorial(10)
# # call factorial()...
# # 3628800
# 复制代码
# 但是，对于参数不是一个的函数，调用将报错。@log写死了只含一个参数的返回函数。
#
# 5、要让@log自适应任何参数定义的函数，可以利用Python的*args和**kw，保证任意个数的参数总是能正常调用：
#
# 可变参数*args表示任何多个无名参数，它是一个tuple；**kwargs表示关键字参数，它是一个dict。并且同时使用*args和**kwargs时，必须*args参数列要在**kwargs前。
#
# 复制代码
# def log(f):
#     def fn(*args, **kw):
#         print 'call ' + f.__name__ + '()...'
#         return f(*args, **kw)
#     return fn
#
# @log
# def add(x, y):
#     return x + y
# print add(1, 2)
# # call add()...
# # 3
# 复制代码
# 6、@performance，它可以打印出函数调用的时间。
#
# 计算函数调用的时间可以记录调用前后的当前时间戳，然后计算两个时间戳的差。
#
# 复制代码
# import time
# def performance(f):
#     def fn(*args, **kw):
#         t1 = time.time()
#         r = f(*args, **kw)
#         t2 = time.time()
#         print 'call %s() in %fs' % (f.__name__, (t2 - t1))
#         return r
#     return fn
#
# @performance
# def factorial(n):
#     return reduce(lambda x,y: x*y, range(1, n+1))
# print factorial(5)
# # call factorial() in 0.000000s
# # 120
# 复制代码
# 7、对于被装饰的函数，log打印的语句是不能变的（除了函数名）。
#
# 如果有的函数非常重要，希望打印出'[INFO] call xxx()...'，有的函数不太重要，希望打印出'[DEBUG] call xxx()...'，这时，log函数本身就需要传入'INFO'或'DEBUG'这样的参数：
#
# 复制代码
# @log('DEBUG')
# def my_func():
#     pass
# #把上面的定义翻译成高阶函数的调用，就是：
# my_func = log('DEBUG')(my_func)
# #上面的语句看上去还是比较绕，再展开一下：
# log_decorator = log('DEBUG')
# my_func = log_decorator(my_func)
# #上面的语句又相当于：
# log_decorator = log('DEBUG')
# @log_decorator
# def my_func():
#     pass
# 复制代码
# 所以，带参数的log函数首先返回一个decorator函数，再让这个decorator函数接收my_func并返回新函数：
#
# 而且wrapper(*args, **kw)要调用外层参数prefix，所以无法拆开
#
# 复制代码
# def log(prefix):
#     def log_decorator(f):
#         def wrapper(*args, **kw):
#             print '[%s] %s()...' % (prefix, f.__name__)
#             return f(*args, **kw)
#         return wrapper
#     return log_decorator
#
# @log('DEBUG')
# def test():
#     pass
# print test()
#
# # [DEBUG] test()...
# # None
# 复制代码
# 8、区别
#
# 复制代码
# #在没有decorator的情况下，打印函数名：
# def f1(x):
#     pass
# print f1.__name__  #f1
#
# #有decorator的情况下，再打印函数名：
# def log(f):
#     def wrapper(*args, **kw):
#         print 'call...'
#         return f(*args, **kw)
#     return wrapper
# @log
# def f2(x):
#     pass
# print f2.__name__  #wrapper
# 复制代码
# 可见，由于decorator返回的新函数函数名已经不是'f2'，而是@log内部定义的'wrapper'。这对于那些依赖函数名的代码就会失效。decorator还改变了函数的__doc__等其它属性。如果要让调用者看不出一个函数经过了@decorator的“改造”，就需要把原函数的一些属性复制到新函数中：
#
# 复制代码
# def log(f):
#     def wrapper(*args, **kw):
#         print 'call...'
#         return f(*args, **kw)
#     wrapper.__name__ = f.__name__
#     wrapper.__doc__ = f.__doc__
#     return wrapper
# 复制代码
# 这样写decorator很不方便，因为我们也很难把原函数的所有必要属性都一个一个复制到新函数上，所以Python内置的functools可以用来自动化完成这个“复制”的任务：
#
# 复制代码
# import functools
# def log(f):
#     @functools.wraps(f)
#     def wrapper(*args, **kw):
#         print 'call...'
#         return f(*args, **kw)
#     return wrapper
# @log
# def f2(x):
#     pass
# print f2.__name__  #f2
# 复制代码
# 9、当一个函数有很多参数时，调用者就需要提供多个参数。如果减少参数个数，就可以简化调用者的负担。
#
# 比如，int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
#
# 但int()函数也提供额外的base参数，默认为10。如果传入base参数，就可以做N进制转换：
#
# print int("10")    #10
# print int('10', 8)  #8
# print int('A', 16)  #10
# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
#
# def int2(x, base=2):
#     return int(x, base)
#
# print int2('1000000')  #64
# print int2('1010101')  #85
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
#
# import functools
# int2 = functools.partial(int, base=2)
#
# print int2('1000000')  #64
# print int2('1010101')  #85
# 所以，functools.partial可以把一个参数多的函数变成一个参数少的新函数，少的参数需要在创建时指定默认值，这样，新函数调用的难度就降低了。
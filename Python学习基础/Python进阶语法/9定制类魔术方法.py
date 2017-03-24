# __author__ = 'yuchunhai'
# 1、__str__()：把一个类的实例变成 str
#
# __repr__()转换为机器看的字符串，可以由eval()执行
#
# 复制代码
# class Person(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#     def __str__(self):
#         return '(Person: %s, %s)' % (self.name, self.gender)
# p = Person('Bob', 'male')
# print p   #(Person: Bob, male)
# 复制代码
# 2、比较运算符_cmp__()：可以实现对一组 Student 类的实例排序
#
# __eq__()判断等于，__lt__()判断小于，__gt__()判断大于
#
# 复制代码
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def __str__(self):
#         return '(%s: %s)' % (self.name, self.score)
#     def __cmp__(self, s):
#         if self.name < s.name:
#             return -1
#         elif self.name > s.name:
#             return 1
#         else:
#             return 0
#
# L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 77)]
# print sorted(L)    #[(Alice: 77), (Bob: 88), (Tim: 99)]
# L = [Student('Tim', 99), Student('Bob', 88), 100, 'Hello']  #list不仅仅包含 Student 类
# print sorted(L)  #报错
# 复制代码
# 上述 Student 类实现了__cmp__()方法，__cmp__用实例自身self和传入的实例 s 进行比较，如果self应该排在前面，就返回 -1，如果s应该排在前面，就返回1，如果两者相当，返回 0。
#
# 3、__len__()：返回元素的个数
#
# 复制代码
# class Students(object):
#     def __init__(self, *args):
#         self.names = args
#     def __len__(self):
#         return len(self.names)
# ss = Students('Bob', 'Alice', 'Tim')
# print len(ss)   #3
# 复制代码
# 4、四则运算：__add__(),__sub__(),__mul__(),__div__()
#
# 逻辑运算 __or__(),__and__()
#
# 复制代码
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
# class Rational(object):
#     def __init__(self, p, q):
#         self.p = p
#         self.q = q
#     def __add__(self, r):
#         return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
#     def __sub__(self, r):
#         return Rational(self.p * r.q - self.q * r.p, self.q * r.q)
#     def __mul__(self, r):
#         return Rational(self.p * r.p, self.q * r.q)
#     def __div__(self, r):
#         return Rational(self.p * r.q, self.q * r.p)
#     def __str__(self):
#         g = gcd(self.p, self.q)
#         return '%s/%s' % (self.p / g, self.q / g)
#     __repr__ = __str__
# r1 = Rational(1, 2)
# r2 = Rational(1, 4)
# print r1 + r2   #3/4
# print r1 - r2   #1/4
# print r1 * r2   #1/8
# print r1 / r2   #2/1
# 复制代码
# 我们也许还有希望覆盖“原位”操作， 比如， __iadd__()。这是用来支持像 mon += tue 这样的操作符，并把正确的结果赋给 mon。重载一个__i*__()方法的唯一秘密是它必须返回 self。把下面的片断加到我们例子中，以修复上面的 repr()问题，并支持增量赋值：
#
# 5、类型转换：__int__(),__float__()
#
# 复制代码
# class Rational(object):
#     def __init__(self, p, q):
#         self.p = p
#         self.q = q
#     def __int__(self):
#         return self.p // self.q
#     def __float__(self):
#         return float(self.p) / self.q
#
# print int(Rational(7, 2))     #3
# print int(Rational(1, 3))     #0
# print float(Rational(7, 2))   #3.5
# print float(Rational(1, 3))   #0.333333333333
# 复制代码
# 6、__slots__():限制当前类所能拥有的属性，能节省内存
#
# 复制代码
# class Person(object):
#     __slots__ = ('name', 'gender')
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
# p = Person('Bob', 'male')
# print p.name  #Bob
# print p.gender   #male
# print p.score  #报错
#
# class Student(Person):
#     __slots__ = ('score',)
#     def __init__(self, name, gender, score):
#         super(Student, self).__init__(name, gender)
#         self.score = score
#
# s = Student('Bob', 'male', 59)
# print s.score   # 59
# 复制代码
# __slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的。除非在子类中也定义__slots__
#
# 7、__call__():
#
# 在Python中，所有的函数都是可调用对象。
#
# 一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()。
#
# 复制代码
# class Person(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#     def __call__(self, friend):
#         print 'My name is %s...' % self.name
#         print 'My friend is %s...' % friend
#
# p = Person('Bob', 'male')
# p('Tim')
# # My name is Bob...
# # My friend is Tim...
# 复制代码
# 单看p('Tim')你无法确定p是一个函数还是一个类实例，所以，在Python中，函数也是对象，对象和函数的区别并不显著。
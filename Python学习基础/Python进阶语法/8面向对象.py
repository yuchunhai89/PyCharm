# __author__ = 'yuchunhai'
# 1、类通过class关键字定义。类名以大写字母开头，紧接着是(object)，表示该类是从哪个类继承下来的。
# 类也要细致命名，像“AddrBookEntry”，“RepairShop”等等就是很好的名字
# Python 并不支持纯虚函数（像 C++）或者抽象方法（如在 JAVA 中）
# class Person(object):
#     pass
# 2、有了Person类的定义，就可以创建出具体的xiaoming、xiaohong等实例。创建实例使用类名+()，类似函数调用的形式创建：
# Python 规范推荐使用骆驼记法的下划线方式，比如，“update_phone”“update_email”。
# xiaoming = Person()
# xiaohong = Person()
# 3、由于Python是动态语言，对每一个实例，都可以直接给他们的属性赋值：
# xiaoming = Person()
# xiaoming.name = 'Xiao Ming'
# xiaoming.gender = 'Male'
# xiaoming.birth = '1990-1-1'
# 4、构造函数__init__()方法
# class Person(object):
#     def __init__(self, name, gender, birth):
#         self.name = name
#         self.gender = gender
#         self.birth = birth
# __init__()方法的第一个参数必须是self（也可以用别的名字，但建议使用习惯用法），后续参数则可以自由指定，和定义函数没有任何区别。
# 相应地，创建实例时，就必须要提供除self以外的参数：
# xiaoming = Person('Xiao Ming', 'Male', '1991-1-1')
# xiaohong = Person('Xiao Hong', 'Female', '1992-2-2')
# print xiaoming.name  # 输出 'Xiao Ming'
# print xiaohong.birth  # 输出 '1992-2-2'
# 定义Person类的__init__方法，除了接受 name、gender 和 birth 外，还可接受任意关键字参数，并把他们都作为属性赋值给实例。
# 要定义关键字参数，使用 **kw；
# 除了可以直接使用self.name = 'xxx'设置一个属性外，还可以通过 setattr(self, 'name', 'xxx') 设置属性。
# 复制代码
# class Person(object):
#     def __init__(self, name, gender, birth, **kw):
#         self.name = name
#         self.gender = gender
#         self.birth = birth
#         for k, v in kw.iteritems():
#             setattr(self, k, v)
# xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')
# print xiaoming.name   #输出Xiao Ming
# print xiaoming.job   #输出Student
# 复制代码
# 5、析构函数
# 由于 Python 具有垃圾对象回收机制（靠引用计数)，这个函数要直到该实例对象所有的引用都被清除掉后才会执行。所以很少用到。
# class Person(object):
#     def __init__(self, ……):
# 6、Python对属性权限的控制是通过属性名来实现的，如果一个属性由双下划线开头(__)，该属性就无法被外部访问。
# 复制代码
# class Person(object):
#     def __init__(self, name):
#         self.name = name
#         self._title = 'Mr'
#         self.__job = 'Student'
# p = Person('Bob')
# print p.name   # => Bob
# print p._title   # => Mr
# print p._Person__job  # => Student  #所以实际上并不是严格的私有成员
# print p.__job   # => Error
# 复制代码
# 但是，如果一个属性以"__xxx__"的形式定义，那它又可以被外部访问了，以"__xxx__"定义的属性在Python的类中被称为特殊属性，有很多预定义的特殊属性可以使用，通常我们不要把普通属性用"__xxx__"定义。
# 以单下划线开头的属性"_xxx"可以在子类中使用，不应该被外部访问，理解为保护成员。
# "__xxx"可以理解为私有成员，但实质并不是，不建议访问。
# 7、类属性是直接绑定在类上的，所以，访问类属性不需要创建实例，就可以直接访问：
# 复制代码
# class Person(object):
#     address = 'Earth'
#     def __init__(self, name):
#         self.name = name
# p1=Person(xiaoming)
# print Person.address   # => Earth
# print p1.address      # => Earth
# # 由于Python是动态语言，类属性也是可以动态添加和修改的：
# Person.address = 'China'
# print p1.address   # => 'China'
# 复制代码
# 8、在实例变量上修改类属性
# 当实例属性和类属性重名时，实例属性优先级高，它将屏蔽掉对类属性的访问。而其他不变
# 9、访问类的属性
# 有两种方法。最简单的是使用 dir()内建函数。另外是通过访问类的字典属性__dict__，这是所有类都具备的特殊属性之一。
# 10、实例的方法。
# 实例的方法就是在类中定义的函数，它的第一个参数永远是self，指向调用该方法的实例本身，其他参数和一个普通函数是完全一样的：在其他语言中,self就是this.
# 复制代码
# class Person(object):
#     def __init__(self, name):
#         self.__name = name
#     def get_name(self):
#         return self.__name
# p1 = Person('Bob')
# print p1.get_name()  # self不需要显式传入  # => Bob
# print p1.__dict__  # {'_Person__name': 'Bob'}
# print p1._Person__name  # => Bob
# 复制代码
# 在实例方法内部，可以访问所有实例属性，这样，如果外部需要访问私有属性，可以通过方法调用获得，这种数据封装的形式除了能保护内部数据一致性外，还可以简化外部调用的难度。
# 11、方法也分实例方法和类方法。
# @classmethod  调用的时候用类名而不是某个对象
# 在class中定义的全部是实例方法，实例方法第一个参数self是实例本身。
# 要在class中定义类方法，需要这么写：
# 复制代码
# class Person(object):
#     count = 0
#     @classmethod
#     def how_many(cls):
#         return cls.count
#
#     def __init__(self, name):
#         self.name = name
#         Person.count = Person.count + 1
#
# print Person.how_many()  #0
# p1 = Person('Bob')
# print Person.how_many()  #1
# 复制代码
# 通过标记一个@classmethod，该方法将绑定到Person类上，而非类的实例。类方法的第一个参数将传入类本身，通常将参数名命名为cls，上面的cls.count实际上相当于Person.count。
# 因为是在类上调用，而非实例上调用，因此类方法无法获得任何实例变量，只能获得类的引用
# 12、@property  像访问属性一样调用方法，即不用括号
# 复制代码
# class Person(object):
#     count = 0
#     def __init__(self, name,age,weight):
#         self.name = name
#         self._age = age
#         self.__weight = weight
#         Person.count = Person.count + 1
#
#     @classmethod
#     def how_many(cls):
#         return cls.count
#
#     @property
#     def get_weight(self):
#         return self.__weight
#
# print Person.how_many()  # 0
# p1 = Person('Bob',20,50)
# print Person.how_many()  # 1
# print p1.get_weight  #50
# 复制代码
# get/set方法：
# 复制代码
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.__score = score
#     def get_score(self):
#         return self.__score
#     def set_score(self, score):
#         if score < 0 or score > 100:
#             raise ValueError('invalid score')
#         self.__score = score
# #但是写 s.get_score() 和 s.set_score() 没有直接写 s.score 来得直接。
# 复制代码
# 　　
#
# 用装饰器函数把get/set方法“装饰”成属性调用:
# 把一个getter方法变成属性，只需要加上 @ property就可以了
# setter是关键字，这种“@+方法名字+点+setter”是个固定格式与@property搭配使用。
# 复制代码
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.__score = score
#     @property
#     def score(self):
#         return self.__score
#     @score.setter
#     def score(self, score):
#         if score < 0 or score > 100:
#             raise ValueError('invalid score')
#         self.__score = score
#
# s = Student("Bob",100)
# print s.score  #100
# s.score = 90    #属性赋值
# print s.score  #90
# 复制代码
# 13、函数和方法
# 函数是直接调用函数名，仅仅是一部分代码
# 方法必须和对象结合在一起使用，是类的一部分
# 方法可以看做是类的属性
# 复制代码
# class Test(object):
#     def test(self):
#         pass
#
# a = Test()
# print a.test  #<bound method Test.test of <__main__.Test object at 0x00000000022B8E10>>
# print a.test() #None
# a.test= "123"
# print a.test #123
# print a.test()  #报错
# 复制代码
# 14、定义子类
# 复制代码
# class Person(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
# class Student(Person):
#     def __init__(self, name, gender, score):
#         super(Student, self).__init__(name, gender)  #初始化
#         self.score = score
# 复制代码
# 一定要用super(Student, self).__init__(name, gender)去初始化父类，否则，继承自Person的Student将没有name和gender。
# 函数super(Student, self)将返回当前类继承的父类，即Person，然后调用__init__()方法，注意self参数已在super()中传入，在__init__()中将隐式传递，不需要写出（也不能写）
# 使用super()的漂亮之处在于，你不需要明确给出任何基类名字，这意味着如果你改变了类继承关系，你只需要改一行代码（class语句本身）而不必在大量代码中去查找所有被修改的那个类的名字。
# 一个实例可以看成它本身的类型，也可以看成它父类的类型。
# 15、多重继承
# 复制代码
# class A(object):
#     def __init__(self, a):
#         print 'init A...'
#         self.a = a
# class B(A):
#     def __init__(self, a):
#         super(B, self).__init__(a)
#         print 'init B...'
# class C(A):
#     def __init__(self, a):
#         super(C, self).__init__(a)
#         print 'init C...'
# class D(B, C):
#     def __init__(self, a):
#         super(D, self).__init__(a)
#         print 'init D...'
# 复制代码
# 像这样，D 同时继承自 B 和 C，也就是 D 拥有了 A、B、C 的全部功能。多重继承通过super()调用__init__()方法时，A 虽然被继承了两次，但__init__()只调用一次：
# 多重继承的目的是从两种继承树中分别选择并继承出子类，以便组合功能使用。
# 举个例子，Python的网络服务器有TCPServer、UDPServer、UnixStreamServer、UnixDatagramServer，而服务器运行模式有多进程ForkingMixin和多线程ThreadingMixin两种。
# 要创建多进程模式的 TCPServer：
# class MyTCPServer(TCPServer, ForkingMixin)
#     pass
# 要创建多线程模式的 UDPServer：
# class MyUDPServer(UDPServer, ThreadingMixin):
#     pass
# 如果没有多重继承，要实现上述所有可能的组合需要 4x2=8 个子类。
#
# 16、多态
# 用一个类继承多个类，调用同一个方法，会有不同的反应，因为被重写了。
# 17、鸭子类型
# 定义：“当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。
# 这种风格适用于动态语言(比如PHP、Python、Ruby、Typescript、Perl、Objective-C、Lua、Julia、JavaScript、Java、Groovy、C#等)和某些静态语言
# 在鸭子类型中，关注的不是对象的类型本身，而是它是如何使用的。例如，在不使用鸭子类型的语言中，我们可以编写一个函数，它接受一个类型为鸭的对象，并调用它的走和叫方法。在使用鸭子类型的语言中，这样的一个函数可以接受一个任意类型的对象，并调用它的走和叫方法。
# 鸭子类型通常得益于不测试方法和函数中参数的类型，而是依赖文档、清晰的代码和测试来确保正确使用。从静态类型语言转向动态类型语言的用户通常试图添加一些静态的（在运行之前的）类型检查，从而影响了鸭子类型的益处和可伸缩性，并约束了语言的动态特性。
# 鸭子类型比接口更好用。
# 复制代码
# class TestClass1:
#     def say(self):
#         print("我是鸭子1")
# class TestClass2:
#     def say(self):
#         print("我是鸭子2")
# def duck_say(duck):
#     duck.say()
# duck_say(TestClass1()) # 我是鸭子1
# duck_say(TestClass2()) # 我是鸭子2
# 复制代码
# 18、getattr()、setattr()和delattr()：
# getattr()和 setattr()函数相应地取得和赋值给对象的属性，
# getattr()会在你试图读取一个不存在的属性时，引发 AttributeError 异常，除非给出那个可选的默认参数。
# setattr()将要么加入一个新的属性，要么取代一个已存在的属性。
# delattr()函数会从一个对象中删除属性
# 复制代码
# class Person(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
# class Student(Person):
#     def __init__(self, name, gender, score):
#         super(Student, self).__init__(name, gender)
#         self.score = score
#     def whoAmI(self):
#         return 'I am a Student, my name is %s' % self.name
#
# s = Student('Bob', 'Male', 88)
# print getattr(s, 'name')  # 获取name属性  #Bob
#
# setattr(s, 'name', 'Adam')  # 设置新的name属性
# print s.name #Adam
# getattr(s, 'age')  # 获取age属性，但是属性不存在，报错：
# getattr(s, 'age', 20)  # 获取age属性，如果属性不存在，就返回默认值20：
# 复制代码
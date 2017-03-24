# __author__ = 'yuchunhai'
# 1、错误类型
# OverflowError数值运算超出最大限制
# ZeroDivisionError 除(或取模)零 (所有数据类型)
# AttributeError对象没有这个属性
# IOError 输入/输出操作失败
# IndexError  序列中没有此索引(index)
# NameError  未声明/初始化对象 (没有属性)
# SyntaxError Python 语法错误
# TypeError 对类型无效的操作
# ValueError 传入无效的参数
# 2、try-except处理异常
# try-except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。
# 复制代码
# try:
# <语句>        #运行别的代码
# except Exception1,e：#Exception是错误类型名，e是储存错误，可以调用
# <语句>        #如果在try部份引发了'名字'异常
# except Exception2,e:
# <语句>        #如果引发了'名字'异常，获得附加的数据
# else:
# <语句>        #如果没有异常发生
# 复制代码
# 当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。
# 复制代码
# try:
#    fh = open("testfile", "w")
#    fh.write("This is my test file for exception handling!!")
# except IOError:
#    print "Error: can\'t find file or read data"
# else:
#    print "Written content in the file successfully"   #Written content in the file successfully
#
# try:
#    fh = open("testfile", "r")  #只读文件不能写入
#    fh.write("This is my test file for exception handling!!")
# except IOError,e:
#    print "Error: can\'t find file or read data"
#    print "catch error:",e
# else:
#    print "Written content in the file successfully"
#    #Error: can't find file or read data
#    #atch error: File not open for writing
# 复制代码
# except若不带任何异常类型，即捕获所有发生的异常。但是不能捕获语法错误异常，如if a,因为是运行前错误而不是运行时错误
# 也可带多种类型except(Exception1[, Exception2[,...ExceptionN]]]):
# 错误类型后面跟着变量e，可以print错误提示
# 案例如下
# 复制代码
# import random
# num = random.randint(0,100)
#
# while 1:
#     try:
#         guess = int(raw_input("Enter 1-100:"))
#     except ValueError,e:
#         print "error ! please enter 1-100"
#         continue
#     if guess > num:
#         print "guess bigger:",guess
#     elif guess < num:
#         print "guess smaller:",guess
#     else:
#         print "guess right,game over"
#         break
# 复制代码
# 3、try-finally语句
# 语句是否发生异常都将执行最后的代码。将异常保留下来交给系统处理，本身不处理异常。
# 作用：为处理异常事件提供清理机制，用来关闭文件或者释放系统资源。
#
# try:
# <语句>
# finally:
# <语句>    #退出try时总会执行
# raise
# 可以使用except语句或者finally语句，但是两者不能同时使用。else语句也不能与finally语句同时使用。
# 4、try-except-finally
# 若try语句没有捕获异常，执行完try代码段后，执行finally
# 若try捕获异常，首先执行except处理异常，然后执行finally
# 5、try-except-else-finally
# 若try语句没有捕获异常，执行完try代码段后，执行else代码段，最后执行finally
# 若try捕获异常，首先执行except处理错误，然后执行finally
# 6、try-finally-except
# 当在try块中抛出一个异常，立即执行finally块代码。
# finally块中的所有语句执行后，异常被再次提出，并执行except块代码。
# 7、with语句
# 用来代替try-except-finally语句，使代码更加简洁
# with context[as var]:
#     with_suite
# context表达式返回是一个对象
# var用来保存context返回对象，单个返回值或元组
# with_suite使用var变量对context返回对象进行操作
# with open("1.text") as f:
#     for line in f.readline():
#         print line
#    1、打开1.txt文件
#    2、f变量接收文件对象返回的对象
#    3、with中的代码执行完成后，关闭文件
# 程序使用了上下文管理器 (with...as...)。上下文管理器有隶属于它的程序块。当隶属的程序块执行结束的时候(也就是不再缩进)，上下文管理器自动关闭了文件
# 运用情况：①文件操作 ②进城之间互斥操作：例如互斥锁  ③支持上下文的其他对象
# 8、raise主动抛出异常
# #格式
# rasie [exception[,args]]
# #Exception 异常类
# #args 描述异常信息的元组
# raise TypeError,"Test Error"  #TypeError: Test Error
# 9、assert语句
# 断言语句：assert语句是用于检测表达式是否为真，如果为假，引发AssertionError错误
# #格式
# assert expression [,args]
# #expression 表达式
# #args 判断条件的描述信息
# 10、自定义异常
# 通过创建一个新的异常类，程序可以命名它们自己的异常。异常应该是典型的继承自Exception类，通过直接或间接的方式。
# 自定义异常只能主动触发。
# 复制代码
# class FileError(IOError):
#     pass
#
# try:
#     raise FileError,"test error"
# except FileError,e:
#     print e  #test error
# class CustomError(Exception):
#     def __init__(self,info):
#         Exception.__init__(self)
#         self.errorinfo = info
#     def __str__(self):
#         return "CustomError:%s" %self.errorinfo
#
# try:
#     raise CustomError("test CustomError")
# except CustomError,e:
#     print "ErrorInfo:",e  #ErrorInfo: CustomError:test CustomError
# 复制代码
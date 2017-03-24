# __author__ = 'yuchunhai'
# 1、pass语句
# pass代表该语句什么都不做，因为python中空代码是非法的，比如一个if语句要求什么内容都不做，我们就可以使用pass语句。
# 2、del语句
# 一般来说python会删除那些不在使用的对象(因为使用者不会再通过任何变量或者数据结构引用它们)
# 3、exec语句（运行字符串中的程序）
# exec "print 'hello world'"  #hello world
# 4、eval函数(会计算python表达式(以字符串形式书写)，并且返回结果)
# print eval('2+ 2')  #4
# print eval(raw_input("please input number:"))  #输入2+2 得4
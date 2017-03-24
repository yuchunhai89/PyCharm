# __author__ = 'yuchunhai'
# #1、变量不需要声明，可以直接输入，大小写敏感
# #2、这里的var = xxxx不叫变量赋值，而叫变量绑定，一个符号可以绑定任意类型的值。
# #3、内置函数type(), 用以查询变量的类型
# var = 1
# print (var)  #1
# print(type(var)) #整数类型 # <type 'int'>
# var = 1.1
# print(var)   #  1.1
# print(type(var))  #浮点数类型  # <type 'float'>
# var = 'hello'
# print(var)  # hello
# print(type(var))  #字符串  # <type 'str'>
# var = (1==1)
# print(var) # True
# print(type(var))  #布尔型  # <type 'bool'>
# var = None
# print(var) # None
# print(type(var))  #空值  # <type 'NoneType'>
# var =(1+1j) #或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型
# print(var) # (1+1j)
# print(type(var))  #复数类型     # <type 'complex'>
# #4、字符串以''或" "括起来的任意文本
# #5、布尔型（True, False，可以用and, or, not运算，而不是C语言的&&和||）
# #6、多变量赋值
# a = b = c = 1
# a, b, c = 1, 2, "john"    #等号两边都是元组，建议加上括号，增加可读性
# #x,y = y,x     #两值交换，不需要temp,更加简洁
# #7、赋值语句不可以返回值，对象是通过引用传递的
# #y =(x = x + 1)#这是非法的
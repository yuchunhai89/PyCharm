# __author__ = 'yuchunhai'
# 1、函数作用域LEGB   L>E>G>B
#
# L:local 函数内部作用域
#
# E：enclosing 函数内部与内嵌函数之间，即闭包
#
# G：global全局作用域
#
# B：bulid-in 内置作用域 list,tuple之类
#
# 复制代码
# passline = 60  #全局
# def func(val):
#     passline = 90  #函数内部
#     if val >= passline:
#         print "pass"
#     else:
#         print "failed"
#     def in_func():
#         print val  #函数内部与内嵌函数之间
#     in_func()
# func(69)
# #failed
# #69
# 复制代码
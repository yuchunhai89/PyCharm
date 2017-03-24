# __author__ = 'yuchunhai'
# 1、位置参数必须以在被调用函数中定义的准确顺序来传递，参数数目必须一致。
#
# 2、所有必需的参数都要在默认参数之前。
#
# 复制代码
# # 位置参数
# def func_with_parameters(x, y):
#     print(x, y)
# func_with_parameters(1, 2)
#
# #默认值参数
# def func_with_default_value_parameters(x, y, z = 3):
#     print(x, y, z)
# func_with_default_value_parameters(y = 2, x = 1)
# 复制代码
# 3、如果命名了参数，这里可以不按顺序给出参数。
#
# #命名参数
# def func_with_named_parameters(x, y, z):
#     print(x, y, z)
# func_with_named_parameters(z = 1, y = 2, x = 3)
# 4、变长的参数在函数声明中不是显式命名的，因为参数的数目在运行时之前是未知的（甚至在运行的期间，每次函数调用的参数的数目也可能是不同的），这和常规参数（位置和默认）明显不同，常规参数都是在函数声明中命名的。由于函数调用提供了关键字以及非关键字两种参数类型，python 用两种方法来支持变长参数。
#
# func(*tuple_grp_nonkw_args, **dict_grp_kw_args)
#
# 其中的 tuple_grp_nonkw_args 是以元组形式体现的非关键字参数组, dict_grp_kw_args 是装有关键字参数的字典。
#
# 5、可变长的参数元组必须在位置和默认参数之后。
#
# # 收集多余的位置参数
# def func_with_collection_rest_parameters(x, y=0, *rest):
#     print(x, y)
#     print(rest)
# func_with_collection_rest_parameters(1, 2, 3, 4, 5)
# 星号操作符之后的形参将作为元组传递给函数,元组保存了所有传递给函数的"额外"的参数(匹配了所有位置和具名参数后剩余的)。如果没有给出额外的参数，元组为空。
#
# 6、关键字变量参数（Dictionary）
#
# 在我们有不定数目的或者额外集合的关键字的情况中， 参数被放入一个字典中，字典中键为参数名，值为相应的参数值。
#
# 复制代码
# #收集命名参数
# def func_with_collection_rest_naned_parameters(*args, **kw):
#     print(args)
#     print(kw)
# func_with_collection_rest_naned_parameters(1, 2, 3, x = 4, y = 5, z = 6)
#
# func_with_collection_rest_naned_parameters([1, 2, 3], {"x": 4, "y": 4, "z": 6})
# #这会导致args[0]指向第一个实参，args[1]指向第二个实参。
# #([1, 2, 3], {'y': 4, 'x': 4, 'z': 6})
# #{}
# func_with_collection_rest_naned_parameters(*[1, 2, 3], **{"x": 4, "y": 4, "z": 6})
# #这里的执行相当于func_with_collection_rest_naned_parameters(1, 2, 3, x = 4, y = 5, z = 6)。
# 复制代码
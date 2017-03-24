__author__ = 'yuchunhai'
# 1、Python代码的缩进规则。具有相同缩进的代码被视为代码块
# 2、缩进请严格按照Python的习惯写法：4个空格，不要使用Tab，更不要混合Tab和空格
# 3、格式
# if  条件1:
#     statement
# elif 条件2:
#     statement
# elif 条件3：
#     statement
# else:
#     statement
#     If后面不需要括号，但是条件后面需要冒号
#     elif 即 else if
# 4、三元运算符
x, y = 4, 3
if x < y:
    result = x
else:
    result = y
print(result)
#等价于
result = x if x < y else y
print(result)

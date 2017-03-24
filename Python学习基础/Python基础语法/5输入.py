__author__ = 'yuchunhai'
x = input()   #1+2
print(type(x))   #<type 'int'>
# y = raw_input()   #1+2
# print(type(y))    # <type 'str'>
#值得注意的是从Python3.2开始，raw_input()已被移除。input的返回类型已经变为str
# 1、由此可见, input() 在对待纯数字输入返回所输入的数字的类型（int，float）
# 而raw_input() 将所有输入作为字符串看待，返回字符串类型。
# 为了避免类型发生错误，一般情况下使用 raw_input() 来与用户交互。
__author__ = 'yuchunhai'
# 1、Python2 里面print可以直接接字符串或者运算。
# 2、Python3 里面print变成了一个函数，上面的写法不支持了，必须用一个括号括起来，否则会报告语法错误。
# 3、>>>是Python解释器的提示符，不是代码的一部分。
# 4、print语句也可以跟上多个字符串，用逗号“,”隔开，遇到逗号“,”会输出一个空格：
# print '1+2=',1+2  #1+2= 3
# 5、多行输出使用三个引号和使用换行符\n一致
# print '''哈
# 哈
# 哈'''
# print "哈\n哈\n哈"
#  输出结果
# 哈
# 哈
# 哈
# 哈
# 哈
# 哈
# 6、转义
# print r'C:\log.txt'
# print 'C:\\log.txt'
# # C:\log.txt
# # C:\log.txt
# 7、print 语句与字符串格式运算符( % )结合使用，可实现字符串替换功能
# print "%s is number %d!" % ("Python", 1)
# %s表示由一个字符串来替换，%d表示由一个整数来替换，%f表示由一个浮点数来替换。
# Python 非常灵活，即使将数字传递给 %s，也不会像其他要求严格的语言一样引发严重后果。
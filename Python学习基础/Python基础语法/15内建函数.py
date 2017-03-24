# __author__ = 'yuchunhai'
# 1、cmp(obj1, obj2) 比较 obj1 和 obj2, 根据比较结果返回整数 i:
#      if obj1 < obj2   返回i < 0
#     if obj1 > obj2   返回i > 0
#     if obj1 == obj2  返回i == 0
#
# 如果是用户自定义对象， cmp()会调用该类的特殊方法__cmp__()
#
# 2、str() 强制转换成字符串
#
# 3、type() :详见（3）数据类型 - 3、
#
# 4、help()：通过用函数名作为 help()的参数就能得到相应的帮助信息
#
# 5、isinstance(变量名，类型)： 判断是否是这个类型的元素，可以用if语句
#
# 6、abs()：取绝对值
#
# 7、enumerate()：详见（10）循环 - 5、
#
# 8、len(seq):返回seq的长度
#
# 9、sorted(iter)：排序，会调用cmp()
#
# 10、zip(a1,a2……):详见（10）循环 - 6、
#
# 11、range():详见（10）循环 - 4、
#
# 12、string.lower()：转换字符串中所有大写字符为小写
#
# 13、string.upper()：转换字符串中所有小写字符为大写
#
# 14、string.strip()：删去字符串开头和结尾的空格
#
# 15、string.capitalize()：把字符串第一个字符大写
#
# 16、string.title()：所有单词都以大写开头
#
# 17、max()和min()：找出最大和最小值
#
# 18、sum()：求和
#
# 19、reversed():倒序输出
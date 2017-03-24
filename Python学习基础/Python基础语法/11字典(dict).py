# __author__ = 'yuchunhai'
# 1、字典的元素没有顺序。你不能通过下标引用元素。字典是通过键来引用，用大括号
# 查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。而list的查找速度随着元素增加而逐渐下降。
# dict的缺点是占用内存大，还会浪费很多内容
# dict是按 key 查找，所以，在一个dict中，key不能重复
# 作为 key 的元素必须不可变
# 2、已知两个列表，一个是名字，一个是成绩，要根据名字找到对应的成绩用两个list不方便，如果把名字和分数关联起来，组成类似的查找表，即 Python中的dict
# 用 dict 表示“名字”-“成绩”的查找表如下：
# 复制代码
# dic = {'tom':11, 'sam':57,'lily':100}
# print type(dic)   #<type 'dict'>
#
# d = {
#     'Adam': 95,
#     'Lisa': 85,
#     'Bart': 59
# }
# print d   #{'Lisa': 85, 'Adam': 95, 'Bart': 59}
# 复制代码
# 3、我们把名字称为key，对应的成绩称为value，dict就是通过 key 来查找 value。
# 4、花括号 {} 表示这是一个dict，然后按照 key: value, 写出来即可。最后一个 key: value 的逗号可以省略。
# 5、由于dict也是集合，len()函数可以计算任意集合的大小：
# print len(d)  #运算结果为3
# 一个 key-value 算一个，因此，dict大小为3。
# 6、可以简单地使用 d[key] 的形式来查找对应的 value，这和 list 很像，不同之处是，list 必须使用索引返回对应的元素，而dict使用key：
# print d['Adam']   #95
# 注意: 通过 key 访问 dict 的value，只要 key 存在，dict就返回对应的value。如果key不存在，会直接报错：KeyError。
# 要避免 KeyError 发生，有两个办法：
#
# 一是先判断一下 key 是否存在，用 in 操作符：
# 二是使用dict本身提供的一个 get 方法，在Key不存在的时候，返回None：
#
#
# print d.get('Bart')  #59
# print d.get('Paul')  #None
# 7、在字典中增添一个新元素的方法：
# 复制代码
# d = {
#     'Adam': 95,
#     'Lisa': 85,
#     'Bart': 59
# }
# print d   #{'Lisa': 85, 'Adam': 95, 'Bart': 59}
# d['lilei'] = 99
# print d   #{'lilei': 99, 'Lisa': 85, 'Adam': 95, 'Bart': 59}
# 复制代码
# 8、循环调用
# 复制代码
# for key in d:   #或for key in d.keys()
#     print d[key]
# # 结果
# # 99
# # 85
# # 95
# # 59
# 复制代码
# 9、字典的常用方法
# print d.keys()          # 返回d所有的键
# print d.values()         # 返回d所有的值
# print d.items()         # 返回d所有的元素（键值对）
# d.clear()            # 清空d，dict变为{}
# del d[‘xxx’]                   # 删除 d 的‘xxx’元素
# for key, value in d.items():
#    print key, ':', value
# 10、cmp()比较
# （1）先比较字典长度
# （2）再比较字典的键
# （3）最后比较字典的值
# （4）都一样就相等
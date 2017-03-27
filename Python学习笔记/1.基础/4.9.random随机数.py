

#随机数
import random

# 生成0至1之间的随机浮点数，结果大于等于0.0，小于1.0
print( random.random() )
# 生成1至10之间的随机浮点数
print( random.uniform(1, 10) )

# 产生随机整数
print( random.randint(1, 5) ) # 生成1至5之间的随机整数，结果大于等于1，小于等于5，前一个参数必须小于等于第二个参数
for i in xrange(5):
    print(i, random.randint(10, 90) ) # 产生 10~90 的随机整数(结果包含 10 和 90)

# 随机选取0到100间的偶数(第二个参数是选取间隔,如果从1开始,就是选取基数)
print( random.randrange(0, 101, 2) )

# 在指定范围内随机选一个值
print( random.choice(range(50)) ) # 这的选值范围是0~49
print( random.choice(['a', 2, 'c']) ) # 从列表中随机挑选一个数，也可以是元组、字符串
print( random.choice('abcdefg') ) # 可从字符串中随机选一个字符
# 在指定范围内随机选多个值(返回一个 list, 第二个参数是要选取的数量)
print( random.sample('abcdefghij',3) )
print( random.sample(['a', 2, 'c', 5, 0, 'ii'],2) )

# 洗牌,让列表里面的值乱序
items = [1, 2, 3, 4, 5, 6]
random.shuffle(items) # 这句改变列表里面的值,返回:None
print( items ) # 输出乱序后的列表


import os
a = os.urandom(16) # 生成16个随机unicode值
print([ord(i) for i in a]) # 打印出来，直接 print a 是无法阅读的

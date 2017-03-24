# __author__ = 'yuchunhai'
# 1、math包主要处理数学相关的运算。math包定义了两个常数:
#
# math.e   # 自然常数e
#
# math.pi  # 圆周率pi
#
# 2、math包运算
#
# math.ceil(x)       # 对x向上取整，比如x=1.2，返回2
#
# math.floor(x)      # 对x向下取整，比如x=1.2，返回1
#
# math.pow(x,y)      # 指数运算，得到x的y次方
#
# math.log(x)       # 对数，默认基底为e。可以使用base参数，来改变对数的基地。
#
# math.sqrt(x)       # 平方根
#
# 3、math包三角函数:
#
# math.sin(x), math.cos(x), math.tan(x), math.asin(x), math.acos(x), math.atan(x)
#
# 这些函数都接收一个弧度(radian)为单位的x作为参数。
#
# 角度和弧度互换: math.degrees(x), math.radians(x)
#
# 4、random包
#
# 1) 随机挑选和排序
#
# random.choice(seq)   # 从序列的元素中随机挑选一个元素
#
# 比如random.choice(range(10)) #从0到9中随机挑选一个整数。
#
# random.sample(seq,k) # 从序列中随机挑选k个元素
#
# random.shuffle(seq)  # 将序列的所有元素随机排序
#
# 2）随机生成实数
#
# random.random()        # 随机生成下一个实数，它在[0,1)范围内。
#
# random.uniform(a,b)      # 随机生成下一个实数，它在[a,b]范围内。
#
# 5、decimal 十进制浮点运算类 Decimal
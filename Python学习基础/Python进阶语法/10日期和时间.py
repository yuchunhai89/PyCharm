# __author__ = 'yuchunhai'
# 1、time包基于C语言的库函数(library functions)。Python的解释器通常是用C编写的，Python的一些函数也会直接调用C语言的库函数。
#
# 2、时间间隔是以秒为单位的浮点小数。
#
# 3、每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
#
# import time;  # 引入time模块
# ticks = time.time()
# print ticks
# 4、获取当前时间
#
# import  time
# localtime = time.localtime(time.time())
# print "本地时间为 :", localtime
# #本地时间为 : time.struct_time(tm_year=2017, tm_mon=2, tm_mday=13, tm_hour=22, tm_min=20, tm_sec=59, tm_wday=0, tm_yday=44, tm_isdst=0)
# #时间元组struct_time：年，月，日，小时，分钟，秒，一周第几天（0是周一），一年第几天，夏令时
# 5、获取格式化时间
#
# 最简单的获取可读的时间模式的函数是asctime():
#
# import time
# localtime = time.asctime( time.localtime(time.time()) )
# print "本地时间为 :", localtime
# #本地时间为 : Mon Feb 13 22:23:57 2017
# 我们可以使用 time 模块的 strftime 方法来格式化日期：
#
# 复制代码
# import time
# # 格式化成2016-03-20 11:45:39形式
# print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# #2017-02-13 22:25:08
# # 格式化成Sat Mar 28 22:24:24 2016形式
# print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
# #Mon Feb 13 22:25:08 2017
# # 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:24 2016"
# print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
# #1459175064.0
# 复制代码
# python中时间日期格式化符号：
#
# %y 两位数的年份表示（00-99）
#
# %Y 四位数的年份表示（000-9999）
#
# %m 月份（01-12）
#
# %d 月内中的一天（0-31）
#
# %H 24小时制小时数（0-23）
#
# %I 12小时制小时数（01-12）
#
# %M 分钟数（00=59）
#
# %S 秒（00-59）
#
# %a 本地简化星期名称
#
# %A 本地完整星期名称
#
# %b 本地简化的月份名称
#
# %B 本地完整的月份名称
#
# %j 年内的一天（001-366）
#
# %U 一年中的星期数（00-53）星期天为星期的开始
#
# %w 星期（0-6），星期天为星期的开始
#
# %W 一年中的星期数（00-53）星期一为星期的开始
#
# 6、获取某月日历
#
# Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
#
# 复制代码
# import calendar
# cal = calendar.month(2017, 2)
# print "以下输出2017年2月份的日历:"
# print cal
# 以下输出2017年2月份的日历:
# #    February 2017
# # Mo Tu We Th Fr Sa Su
# #        1  2  3  4  5
# #  6  7  8  9 10 11 12
# # 13 14 15 16 17 18 19
# # 20 21 22 23 24 25 26
# # 27 28
# 复制代码
# 7、time.sleep(secs)：推迟调用线程的运行，secs指秒数。
#
# import time
# print('start')
# time.sleep(3)     # sleep for 3 seconds
# print('wake up')
# 8、datetime包
#
# datetime包是基于time包的一个高级包， 为我们提供了多一层的便利。
#
# datetime可以理解为date和time两个组成部分。date是指年月日构成的日期(相当于日历)，time是指时分秒微秒构成的一天24小时中的具体时间(相当于手表)。
#
# import datetime
# t = datetime.datetime(2017,2,13,21,30)
# print(t)#2017-02-13 21:30:00
# datetime包还定义了时间间隔对象(timedelta)。一个时间点(datetime)加上一个时间间隔(timedelta)可以得到一个新的时间点(datetime)。同理，两个时间点相减会得到一个时间间隔。
#
# 复制代码
# import datetime
# t      = datetime.datetime(2017,2,13,21,30)
# t_next = datetime.datetime(2017,2,13,23,30)
# delta1 = datetime.timedelta(seconds = 600)
# delta2 = datetime.timedelta(weeks = 3)
# print(t + delta1) #2017-02-13 21:40:00
# print(t + delta2) #2017-03-06 21:30:00
# print(t_next - t) #2:00:00
# 复制代码
# 9、其他模块：pytz模块、dateutil模块
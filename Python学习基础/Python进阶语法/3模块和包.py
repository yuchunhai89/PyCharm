# __author__ = 'yuchunhai'
# 1、概念介绍
#
# #test.py  自身模块名test
#
# import p1.util  引用p1包的模块util
#
# print p1.util.f(2)  调用p1.util的函数f()
#
# 如何区分包和普通目录 包下面有个__inti__.py文件
#
# 2、如果我们只希望导入用到的math模块的某几个函数，而不是所有函数，可以用下面的语句：
#
# from math import pow, sin, log
# 3、可以给函数起个“别名”来避免冲突：as
#
# from math import log
# from logging import log as logger   # logging的log现在变成了logger
# print log(10)   # 调用的是math的log
# logger(10, 'import from logging')   # 调用的是logging的log
# 4、如果导入的模块不存在，Python解释器会报 ImportError 错误：
#
# 5、第三方模块管理系统
#
# -easy_install
#
# -pip(推荐，已内置到Python2.7.9)
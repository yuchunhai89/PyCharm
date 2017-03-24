# __author__ = 'yuchunhai'
# 1、文件也是一个对象。
# 2、打开文件
# f = open(文件名，模式)
# 文件名可以是相对路径或者绝对路径
# 模式有："r" 只读、“w” 写入、“a” 追加，“r+/w+”读写
#
# 使用 'r' 或 'U' 模式打开的文件必须是已经存在的。 使用 'w' 模式打开的文件若存在则首先清空, 然后(重新)创建。 以 'a' 模式打开的文件是为追加数据作准备的, 所有写入的数据都将追加到文件的末尾。 即使你 seek 到了其它的地方。 如果文件不存在, 将被自动创建, 类似以 'w'模式打开文件。
# test = open("test.txt", "w")
# 3、属性
# test = open("test.txt", "w")
# print "文件名: ", test.name   #文件名:  test.txt
# print "是否已关闭 : ", test.closed  #是否已关闭 :  False
# print "访问模式 : ", test.mode  #访问模式 :  w
# 4、关闭 close()
# test = open("test.txt", "w")
# test.close()
# print "是否已关闭 : ", test.closed  #是否已关闭 :  True
# 5、写入write()
# write()方法可将任何字符串写入一个打开的文件。
# write()方法不在字符串的结尾不添加换行符('\n')：
# test = open("test.txt", "w")
# test.write("this is a test\n this is a test again \n")
# test.close()
# #可以在文件中看到
# # this is a test
# # this is a test again
# 主动调用close()写缓存同步到磁盘，或者写入数据量大于或等于写缓存，写缓存同步到磁盘
# 6、读取 read()、readline()、readlines()
# read（size）方法从一个打开的文件中读取一个字符串。size若不填则为尽量多的字符串，若填了则为结束位置。
# readline()读取当前行,允许有参数
# readlines()读取剩余行，返回一个字符串列表
# 复制代码
# test = open ("test.txt", "w")
# test.write("python is a language \npython is a great language ")
# test.close()
# test = open("test.txt", "r")
# str = test.read()
# print str
# test.close()
# #python is a language
# #python is a great language
# 复制代码
# 7、文件位置
# tell()方法告诉你文件内的当前位置；即下一次的读写会发生在文件开头这么多字节之后：
# seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。
# 复制代码
# test = open ("test.txt", "w")
# test.write("python is a language \npython is a great language ")
# test.close()
# test = open("test.txt", "r")
# str = test.read()
# print "the first input:\n",str
# #输出
# # the first input:
# # python is a language
# # python is a great language
# # 查找当前位置
# position = test.tell()
# print position
# #50
# # 把指针再次重新定位到文件开头
# position = test.seek(0, 0)
# str2 = test.read(10)
# print "the second input:\n", str2
# # the second input:
# # python is
# test.close()
# 复制代码
# 8、重命名
# Python的os模块提供了帮你执行文件处理操作的方法，必须先导入它，才可以调用。
# os.rename(当前文件名,新的文件名)
# 9、删除文件
# 同样需要导入os模块，才可以调用。
# os.remove(文件名)
# __author__ = 'yuchunhai'
# 1、匹配字符串
#
# str.startswith()和str.endswith()
#
# 一个句子结尾是\n来结束的，所以用endswith（‘’）方法匹配时要注意传入的变量带有\n
#
# 或者用切片操作，str[:-1].endswith()
#
# 复制代码
# def find(fname):
#     f = open(fname,"r+")
#     for line in f :
#         if line.startswith("this")\    #一个句子太长时使用 \ 符号来换行
#                 or line[:-1].endswith("apple"):
#             print line
#
# find("test1.txt")
# # this is an apple
# # this is a pear
# # this is a banana
# # that is an apple
# 复制代码
# 2、正则表达式概念
#
# 使用单个字符串来描述匹配一系列符合某个句法规则的字符串，是对字符串操作的一种逻辑公式，应用场景在处理文本和数据。
#
# re 模块使Python语言拥有全部的正则表达式功能。
#
# 3、导入re模块  #import re
#
# 利用re.compile(正则表达式)返回pattern
#
# 利用pattern.match(待匹配字符串)返回match
#
# match.group()返回子串
#
# match.string()返回主串
#
# match.span()返回子串在主串中的位置
#
# 复制代码
# import re
# str1 = "this is an apple"
# regex = re.compile(r"this")  #r‘ ’内的字符不转义
# print regex   #<_sre.SRE_Pattern object at 0x0000000001D2DDD8>
# ma = regex.match(str1)
# print ma  #<_sre.SRE_Match object at 0x0000000002075510>
# print ma.group()  #this
# print ma.span()  #(0, 4)
# print ma.string  #this is an apple
# print ma.re    #=regex
# 复制代码
# 4、re.match 尝试从字符串的开始匹配一个模式。
#
# re.match(pattern, string, flags=0)
# pattern  匹配的正则表达式
#
# string 要匹配的字符串
#
# flags 标志位，用于控制正则表达式的匹配方式，如:是否区分大小写， 多行匹配等等
#
# 匹配成功re.match方法返回一个匹配的对象，否则返回None。
#
# 5、group(num)或groups()匹配对象函数来获取匹配表达式。
#
# group(num=0)匹配的整个表达式的字符串，group()可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
#
# groups()返回一个包含所有小组字符串的元组。
#
# 6、基本匹配符
#
# ①.      匹配任意字符（除了\n）,一个点只是一个字符
#
# ②[…]   匹配字符集   如[a-z][A-Z][0-9][a-zA-Z0-9]
#
# ③[^…]  匹配不在[]中的任意字符
#
# ④\d     匹配数字等价于[0-9]
#
# ⑤\D     匹配非数字
#
# ⑥\s     匹配空白，包括空格、制表符、换页符等等。等价于[\f\n\r\t\v]
#
# ⑦\S     匹配非空白
#
# ⑧\w     匹配单词字符，匹配包括下划线的任何单词字符。等价于[A-Za-z0-9_]
#
# ⑨\W     匹配非单词字符
#
# import re
# ma = re.match(r'[\w]','0')
# print ma.group()#0
# ma = re.match(r'\[[\w]\]','[0]')
# print ma.group()#[0]
# 7、特殊匹配符
#
# ①*      匹配前一个字符0次或无限次
#
# ②+      匹配前一个字符1次或无限次
#
# ③？     匹配前一个字符0次或1次
#
# ④{m}    匹配前一个字符m次
#
# ⑤{m,n}  匹配前一个字符m到n次
#
# ⑥*?或+?或?? 匹配模式变为非贪婪（尽可能减少匹配字符）
#
# 复制代码
# import re
# ma = re.match(r'[a-zA-Z0-9]*','SAFGAFG')
# print ma.group()  #SAFGAFG
# ma = re.match(r'[a-zA-Z0-9]{3,6}@163.com','SAFGFG@163.com')
# print ma.group()  #SAFGFG@163.com
# ma = re.match(r'[0-9][a-z]*','1bc')
# print ma.group()  #1bc
# ma = re.match(r'[0-9][a-z]*?','1bc')
# print ma.group()  #1
# 复制代码
# 8、高级匹配符
#
# ①^      匹配字符串开头
#
# ②$      匹配字符串结尾
#
# ③\A     指定的字符串必须出现在开头
#
# ④\Z     指定的字符串必须出现在结尾
#
# ⑤|      或，匹配左右任意一个表达式
#
# ⑥(ab)   括号中表达式作为一个分组
#
# ⑦\<number>  引用编号为num的分组匹配到的字符串
#
# ⑧(?P<name>) 分组起一个别名
#
# ⑨(?P=name)  引用别名为name的分组匹配字符串
#
# 复制代码
# import re
# ma = re.match(r'^[\w]{4,10}@163.com$',"abc123@163.com")
# print ma.group()  #abc123@163.com
# ma = re.match(r'\Aabc[\w]*',"abc123")
# print ma.group() #abc123
# ma = re.match(r'[1-9]?\d$',"99")#0-99
# print ma.group()  #99
# ma = re.match(r'[1-9]?\d$|100',"100")#0-99
# print ma.group()  #100
# ma = re.match(r'[\w]{4,6}@(163|126|qq).com',"abc123@qq.com")
# print ma.group()  #abc123@qq.com
# ma = re.match(r'<([\w]+>)[\w]+</\1',"<book>python</book>")
# print ma.group()  #<book>python</book>
# ma = re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)',"<book>python</book>")
# print ma.group()  #<book>python</book>
# ma = re.match(r'<(?P<ht>[\w]+>)<(?P<h>[\w]+>)<(?P<s>[\w]+>).+</(?P=s)</(?P=h)</(?P=ht)',"<html><head><script>javascript:alect('hello world')</script></head></html>")
# print ma.group()  #<html><head><script>javascript:alect('hello world')</script></head></html>
# print ma.groups()  #('html>', 'head>', 'script>')
# 复制代码
# 9、其他方式
#
# ①search(pattern,string,flags=0)
#
# 会在字符串内查找模式匹配，直到找到第一个匹配
#
# 匹配成功re.search方法返回一个匹配的对象，否则返回None
#
# ②findall(pattern,string,flags=0)
#
# 找到匹配，返回所有匹配部分的列表
#
# ③sub(pattern,repl,string,count=0,flags=0)
#
# 将字符串中匹配正则表达式的部分替换为其他值
#
# ④split(pattern,string,maxsplit=0,flags=0)
#
# 根据匹配分割字符串，返回分割字符串组成的列表
#
# 复制代码
# import re
# str1 = "abc = 100"
# info = re.search(r'\d+',str1)
# print info.group()  #100
# str2 = "c++=100,java=90,python=80"
# info = re.search(r'\d+',str2)
# print info.group()  #100
# info = re.findall(r'\d+',str2)
# print info  #['100', '90', '80']
# print sum([int(x) for x in info])  #270 #列表解析
#
# str3 = "python video = 1000"
# info = re.sub(r'\d+',"1001",str3)  #sub是调用findall而不是search
# print info  #python video = 1001
#
# def add3(match):
#     val = match.group()
#     num = int(val)+3
#     return str(num)
# info = re.sub(r'\d+',add3,str3)
# print info  #python video = 1001
#
# str4 = "class:C C++ JAVA Python C#"
# info = re.split(r':| |,',str4)
# print info #['class', 'C', 'C++', 'JAVA', 'Python', 'C#']
# 复制代码
# 10、修饰符
#
# 正则表达式可以包含一些可选标志修饰符来控制匹配的模式。修饰符被指定为一个可选的标志。多个标志可以通过按位 OR(|) 它们来指定。
#
# ①re.I     使匹配对大小写不敏感
#
# ②re.M     多行匹配，影响 ^和$
#
# ③re.S     使.匹配包括换行在内的所有字符
#
# 11、抓取网页中的图片到本地
#
# 1：抓取网页
#
# 2：获取图片地址
#
# 3：抓取图片内容并保存到本地
#
# 复制代码
# import urllib2,re
# req = urllib2.urlopen("http://www.imooc.com/course/list")
# buf = req.read()
# listurl = re.findall(r'http:.+\.jpg',buf)
#
# i = 0
# for url in listurl:
#     f = open(str(i)+".jpg","wb")
#     req = urllib2.urlopen(url)
#     buf = req.read()
#     f.write(buf)
#     i+=1
#     print I  #看看输出了多少个，此时也生成i个.jpg
# 复制代码
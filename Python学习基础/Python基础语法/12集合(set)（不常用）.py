# __author__ = 'yuchunhai'
# 1、dict的作用是建立一组 key 和一组 value 的映射关系，dict的key是不能重复的。
# 有的时候，我们只想要 dict 的 key，不关心 key 对应的 value，目的就是保证这个集合的元素不会重复，这时，set就派上用场了。
# 2、set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。
# 3、创建 set 的方式是调用 set() 并传入一个 list，list的元素将作为set的元素：
# s = set(['A', 'B', 'C'])
# print s  #set(['A', 'C', 'B'])
# 4、添加、删除：
# s.add('D')
# print s  #set(['A', 'C', 'B', 'D'])
# s.add('D') #已存在不会报错
# s.remove('D')
# print s  #set(['A', 'C', 'B'])
# s.remove('D')  #报错，需要先判断
Python����ģʽ��ʵ�ַ���

�����ȶ�������������������ͣ�
    __new__ �������õ� class ��Ϊ���һ���������ú����Ĺ��������Ƿ������һ����ʵ����
    __init__ �������õ�ʵ����Ϊ���һ�����������������κζ���;��ְ���ǳ�ʼ��ʵ����
    __call__ ����ģ����ĵ��ã��൱�������������������


### ����1 ###
  #����1,��������
    #��ν����������������(ʵ��������)ӵ����ͬ��״̬(����)����Ϊ(����)�������ж�ʱ������ͬ��
    #ͬһ���������ʵ����Ȼӵ����ͬ����Ϊ(����),
    #ֻ��Ҫ��֤ͬһ���������ʵ��������ͬ��״̬(����)����
    #����ʵ���������Ե������ֱ�ӵķ�������__dict__����ָ��(����)ͬһ���ֵ�(dict)
    class Borg(object):
        _state = {}
        def __new__(cls, *args, **kw):
            ob = super(Borg, cls).__new__(cls, *args, **kw)
            ob.__dict__ = cls._state
            return ob

    class MyClass2(Borg):
        a = 1

    one = MyClass2()
    two = MyClass2()

    #one��two��������ͬ�Ķ���,id, ==, is�ԱȽ���ɿ���
    two.a = 3
    print( one.a ) # 3
    print( id(one) ) # 28873680
    print( id(two) ) # 28873712
    print( one == two ) # False
    print( one is two ) # False
    #����one��two������ͬ�ģ�ͬһ��__dict__���ԣ�,��:
    print( id(one.__dict__) ) # 30104000
    print( id(two.__dict__) ) # 30104000

    '''
    ���ۣ�
    ��������������ɵ�ʵ���Ƿ����ͬһid����ֻ������״̬(����)����Ϊ��ʽ(����)ʱ���������ⷽ����
    �ӣ� ��ʵ������ͬһ�������ж�ʱ������ͬ���ϸ���������Ⲣ�ǵ�����
    '''


### ����2 ###
  #����2:ʹ��װ����(decorator)��
    #�����౾�������֪���Լ��ǵ�����,��Ϊ������(�Լ��Ĵ���)�����ǵ�����
    def singleton(cls, *args, **kw):
        instances = {}
        def _singleton():
            if cls not in instances:
                instances[cls] = cls(*args, **kw)
            return instances[cls]
        return _singleton

    @singleton
    class MyClass(object):
        a = 1
        def __init__(self, x=0):
            self.x = x

    one = MyClass()
    two = MyClass()

    two.a = 3
    print( one.a ) # 3
    print( id(one) ) # 29660784
    print( id(two) ) # 29660784
    print( one == two ) # True
    print( one is two ) # True
    one.x = 1
    print( one.x ) # 1
    print( two.x ) # 1

    '''
    ���ۣ�
    ��ԭ������˵�����ǰ�һ����Ľ��ж���͵������Ϊһ��������
        �ú������յ����ߴ���ĳ�ʼ���Ĳ���������黺�����Ƿ��Ѿ����˸���Ķ���
        ���û�и����ʵ�����򴴽�һ�����뻺�沢����ʵ�������йز�����ȫ���ⲻ�ڴ˷�������
        ����ȥ�������ǵ�Ҫ��ֻ�轫���������֮�Ϸ���һ��װ�������ɡ�
    �ӣ� �಻���ٴα��̳С�

    ԭ��������౻װ�ι�֮�󣬾ͻ᷵��һ���������������౾������֮�󱻼̳е�ʱ����������ᱨ�쳣����Ϊ�ⵥ���౾������˵��һ��method�����ࡣ
    ��ȱ��ʹ���಻���ٴα��̳У��ڴ�����д���кܴ�ľ����ԣ���ˬ��
    '''


### ����3 ###
  #����3,ʵ��__new__��������д������Ĺ���(���� new һ����ʵ���Ĺ���)
    #���ڽ�һ�����ʵ���󶨵������_instance��,
    #���cls._instanceΪNone˵�����໹û��ʵ������,ʵ��������,������
    #���cls._instance��ΪNone,ֱ�ӷ���cls._instance
    class Singleton(object):
        # __new__ ������ __init__ ִ�У� ���ײ��� cls �� MyClass�� ������ MyClass��ʵ����
        # __new__ ��һ���෽�����ڴ�������ʱ���á��� __init__ �������ڴ��������󣬵���ʱ�Ե�ǰ�����ʵ����һЩ��ʼ�����޷���ֵ��
        # �����д�� __new__ ���� __new__ ����û�е��� __init__ ����û�з���ʵ��,��ô __init__ ���������á�
        def __new__(cls, *args, **kw):
            if not hasattr(cls, '_instance'):
                orig = super(Singleton, cls)
                cls._instance = orig.__new__(cls, *args, **kw)
            return cls._instance

    # ֻҪ�̳� Singleton �Ϳ���ʵ�ֵ����� Singleton �����ж����ͬ�ĵ��������һ������š�
    class MyClass(Singleton):
        a = 1
        def __init__(self):
            print('------init ------') # �����ж�ִ���˶��ٴ� init ����

    class MyClass2(MyClass):
        pass

    one = MyClass2() # ��ӡ��һ�� init
    two = MyClass2() # �ִ�ӡ��һ�� init

    two.a = 3
    print( one.a ) # 3
    #one��two��ȫ��ͬ,������id(), ==, is���
    print( id(one) ) # 29097904
    print( id(two) ) # 29097904
    print( one == two ) # True
    print( one is two ) # True

    '''
    ���ۣ�
    ������Ĳ��Խ�����Կ�����
        1. ���Ա����ؼ̳С�
        2. û�ж��ʵ��������

    �ƺ��������ǵ�Ҫ�󣬵�������ȱ�ݣ�
        __init__ ��������ε��ã������ˣ���Ȼ��δ��������Ķ���һ�����󣬵��Ǹö���������ÿһ��ʵ�����Ĺ����ж��ᱻ����һ�Σ������������ֻ������һ�β���е�󰡣������о����˼·Ӧ���ǶԵġ�

    �ӣ� ʵ���ظ�����__init__()��ϰ�������ǵĳ�ʼ�����붼�Ƿ��������������ġ�
    '''


### ����4 ###
  #����4:ʹ��__metaclass__��Ԫ�ࣩ�ĸ߼�python�÷��� ע��ֻ�� py2.x ���У� py3.x ���С�
    #�������Ƿ���2������������˵�߼�����
    class Singleton(type):
        # __init__ ������ __call__ ִ�У� ���ײ��� cls �� MyClass�� ������ MyClass��ʵ��(��Ϊ����Ԫ��)��ֻ�ڶ��� MyClass�� ʱִ��һ�Σ���������ִ�С�
        def __init__(cls, name, bases, dct):
            super(Singleton, cls).__init__(name, bases, dct)
            cls._instance = None

        # ÿ�� new MyClass�� ʱ����ִ�У� ���ײ��� cls �� MyClass�� ������ MyClass��ʵ��(��Ϊ����Ԫ��)��
        def __call__(cls, *args, **kw):
            if cls._instance is None:
                cls._instance = super(Singleton, cls).__call__(*args, **kw)
            return cls._instance

    class MyClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            print('------init ------') # �����ж�ִ���˶��ٴ� init ����

    class MyClass2(MyClass):
        pass

    one = MyClass2() # ��ӡ��һ�� init
    two = MyClass2() # ���ٴ�ӡ init

    two.a = 3
    print( one.a ) # 3
    print( id(one) ) # 31495472
    print( id(two) ) # 31495472
    print( one == two ) # True
    print( one is two ) # True

    '''
    ���ۣ�
    ������Ĳ��Խ�����Կ�����
        1. ���Ա����ؼ̳С�
        2. û�ж��ʵ��������
        3. __init__ ����Ҳֻ�ǵ��ù�һ�Ρ�
    '''




�����Ƿǳ��淽��

### ʹ��ģ�� ###
    # python�е� ģ��module �ڳ�����ֻ������һ�Σ�������ǵ����ġ�
    # ����ֱ��дһ��ģ�飬������Ҫ�ķ��������ԣ�д��ģ���е���������ģ���������ȫ�ֱ������ɣ���������Ҫд�ࡣ
    # ���һ���һЩ�ۺ�ģ�������ŵ�ķ�����
    class _singleton(object):
        class ConstError(TypeError):
            pass
        def __setattr__(self,name,value):
            if name in self.__dict__: # �����Ƕ�θ�ֵʱ���쳣�� ʵ���в����������á�
                raise self.ConstError
            self.__dict__[name]=value
        def __delattr__(self,name):
            if name in self.__dict__:
                raise self.ConstError
            raise NameError
    import sys
    sys.modules[__name__]=_singleton()

    # python ������� sys.modules ���м����ȷ��������ģ���������������һ�㽫ģ�����һ������󣬶����Ժ󶼻����ͬһ�������ˡ�
    # ����������single.py�У�

    >>> import single
    >>> single.a=1
    >>> single.a=2
    ConstError
    >>> del single.a
    ConstError


### �������� ###
    class singleton(object):
        pass
    singleton=singleton()
    # ������singleton�󶨵�ʵ���ϣ�singleton�������Լ����Ψһ�����ˡ�
    # ��������Ҳ�Ͳ����� new ������󣬶���ֱ�ӵ��ɱ������ã��о����е�֡�


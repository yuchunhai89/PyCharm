Ԫ��(metaclass)

��ע������һƪ�� Stack overflow �Ϻ��ȵ����ӡ�
    �������Գ��Ѿ��������й�Python OOP����еĸ��ָ����ʼ�վ���Ԫ��(metaclass)������⡣
    ��֪����϶�����ʡ�йأ�����Ȼ���ò�̫���ף�ϣ����ҿ��Ը���һЩʵ�ʵ����Ӻʹ���Ƭ���԰�����⣬�Լ���ʲô�������Ҫ����Ԫ��̡�
    ����e-satisͬѧ��������һ��Ļظ����ûظ������985�����ͬ����������������˵��λظ�Ӧ�ü��뵽Python�Ĺٷ��ĵ���ȥ��
    ��e-satisͬѧ������ Stack Overflow �е���������Ҳ�ߴ�64271�֡�
    ���¾�����ƪ���ʵĻظ�����ʾ���ǳ�����

��Ҳ�Ƕ���
    �����Ԫ��֮ǰ������Ҫ������Python�е��ࡣ
    Python����ĸ������� Smalltalk �����Ե���Щ���ء�
    �ڴ������������У������һ�����������������һ������Ĵ���Ρ�
    ��Python����һ����Ȼ������

        >>> class ObjectCreator(object):
        ��       pass
        ��
        >>> my_object = ObjectCreator()
        >>> print my_object
        <__main__.ObjectCreator object at 0x8974f2c>

    ���ǣ�Python�е��໹Զ��ֹ��ˡ���ͬ��Ҳ��һ�ֶ����ǵģ�û�����Ƕ���
    ֻҪ��ʹ�ùؼ��� class, Python��������ִ�е�ʱ��ͻᴴ��һ������
    ����Ĵ���Σ�

        >>> class ObjectCreator(object):
        ��       pass
        ��

    �����ڴ��д���һ���������־���ObjectCreator��
    ��������ࣩ����ӵ�д���������ʵ�������������������Ϊʲô����һ�����ԭ��
    ���ǣ����ı�����Ȼ��һ���������Ǻ�����Զ��������µĲ�����
        1)   ����Խ�����ֵ��һ������
        2)   ����Կ�����
        3)   �����Ϊ����������
        4)   ����Խ�����Ϊ�����������д���

    ������ʾ����

        >>> print ObjectCreator # ����Դ�ӡһ���࣬��Ϊ����ʵҲ��һ������
        <class '__main__.ObjectCreator'>
        >>> def echo(o):
        ��       print o
        ��
        >>> echo(ObjectCreator) # ����Խ�����Ϊ������������
        <class '__main__.ObjectCreator'>
        >>> print hasattr(ObjectCreator, 'new_attribute')
        False
        >>> ObjectCreator.new_attribute = 'foo' #  �����Ϊ����������
        >>> print hasattr(ObjectCreator, 'new_attribute')
        True
        >>> print ObjectCreator.new_attribute
        foo
        >>> ObjectCreatorMirror = ObjectCreator # ����Խ��ำֵ��һ������
        >>> print ObjectCreatorMirror()
        <__main__.ObjectCreator object at 0x8997b4c>


��̬�ش�����
    ��Ϊ��Ҳ�Ƕ��������������ʱ��̬�Ĵ������ǣ����������κζ���һ����
    ���ȣ�������ں����д����࣬ʹ�� class �ؼ��ּ��ɡ�

        >>> def choose_class(name):
        ��       if name == 'foo':
        ��           class Foo(object):
        ��               pass
        ��           return Foo # ���ص����࣬�������ʵ��
        ��       else:
        ��           class Bar(object):
        ��               pass
        ��           return Bar
        ��
        >>> MyClass = choose_class('foo')
        >>> print MyClass # �������ص����࣬�������ʵ��
        <class '__main__'.Foo>
        >>> print MyClass() # �����ͨ������ഴ����ʵ����Ҳ���Ƕ���
        <__main__.Foo object at 0x89c6d4c>

    ���⻹������̬����Ϊ����Ȼ��Ҫ�Լ���д������Ĵ��롣
    ������Ҳ�Ƕ����������Ǳ�����ͨ��ʲô���������ɵĲŶԡ�
    ����ʹ�� class �ؼ���ʱ��Python�������Զ������������
    ���ͺ�Python�еĴ��������һ����Python��Ȼ�ṩ�����ֶ�����ķ�����
    ���ǵ��ڽ����� type ��������ϵ�ǿ��ĺ����ܹ�����֪��һ�������������ʲô������������

        >>> print type(1)
        <type 'int'>
        >>> print type("1")
        <type 'str'>
        >>> print type(ObjectCreator)
        <type 'type'>
        >>> print type(ObjectCreator())
        <class '__main__.ObjectCreator'>

    ��� type ��һ����ȫ��ͬ����������Ҳ�ܶ�̬�Ĵ����ࡣ type ���Խ���һ�����������Ϊ������Ȼ�󷵻�һ���ࡣ
    ����֪�������ݴ�������Ĳ�ͬ��ͬһ������ӵ��������ȫ��ͬ���÷���һ����ɵ�����飬������Python����Ϊ�˱����������ԣ�

    type ����������������
    type(����, �����Ԫ�飨��Լ̳е����������Ϊ�գ����������Ե��ֵ䣨���ƺ�ֵ��)
    ��������Ĵ��룺

        >>> class MyShinyClass(object):
        ��       pass

    �����ֶ�������������

        >>> MyShinyClass = type('MyShinyClass', (), {}) # ����һ�������
        >>> print MyShinyClass
        <class '__main__.MyShinyClass'>
        >>> print MyShinyClass() #  ����һ�������ʵ��
        <__main__.MyShinyClass object at 0x8997cec>

    ��ᷢ������ʹ�á�MyShinyClass����Ϊ����������Ҳ���԰�������һ����������Ϊ������á�
    ��ͱ����ǲ�ͬ�ģ�����û���κ����ɰ�����Ū�ĸ��ӡ�
    type ����һ���ֵ���Ϊ�ඨ�����ԣ����

        >>> class Foo(object):
        ��       bar = True

    ���Է���Ϊ��

        >>> Foo = type('Foo', (), {'bar':True})

    ���ҿ��Խ�Foo����һ����ͨ����һ��ʹ�ã�

        >>> print Foo
        <class '__main__.Foo'>
        >>> print Foo.bar
        True
        >>> f = Foo()
        >>> print f
        <__main__.Foo object at 0x8a9b84c>
        >>> print f.bar
        True

    ��Ȼ��������������̳У����ԣ����µĴ��룺

        >>> class FooChild(Foo):
        ��       pass

    �Ϳ���д�ɣ�

        >>> FooChild = type('FooChild', (Foo,),{})
        >>> print FooChild
        <class '__main__.FooChild'>
        >>> print FooChild.bar # bar��������Foo�̳ж���
        True

    �������ϣ��Ϊ��������ӷ�����ֻ��Ҫ����һ������ǡ��ǩ���ĺ�����������Ϊ���Ը�ֵ�Ϳ����ˡ�

        >>> def echo_bar(self):
        ��       print self.bar
        ��
        >>> FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
        >>> hasattr(Foo, 'echo_bar')
        False
        >>> hasattr(FooChild, 'echo_bar')
        True
        >>> my_foo = FooChild()
        >>> my_foo.echo_bar()
        True

    ����Կ�������Python�У���Ҳ�Ƕ�������Զ�̬�Ĵ����ࡣ
    ����ǵ���ʹ�ùؼ��� class ʱPython��Ļ���������飬�������ͨ��Ԫ����ʵ�ֵġ�


����ʲô��Ԫ�ࣨ���ڵ������ˣ�
    Ԫ���������������ġ���������
    �㴴�������Ϊ�˴������ʵ�����󣬲�����
    ���������Ѿ�ѧϰ����Python�е���Ҳ�Ƕ���
    �ðɣ�Ԫ���������������Щ�ࣨ���󣩵ģ�Ԫ���������࣬������������ Ϊ��

        MyClass = MetaClass()
        MyObject = MyClass()

    ���Ѿ������� type ������������������

        MyClass = type('MyClass', (), {})

    ������Ϊ���� type ʵ������һ��Ԫ�ࡣ
    type ����Python�ڱ������������������Ԫ�ࡣ
    ��������֪����Ϊʲô type ��ȫ������Сд��ʽ������ Type �أ�
    �ðɣ��Ҳ�����Ϊ�˺� str ����һ���ԣ� str �����������ַ���������࣬�� int ��������������������ࡣ
    type ���Ǵ����������ࡣ�����ͨ����� __class__ ������������һ�㡣
    Python�����еĶ�����ע�⣬����ָ���еĶ����������Ƕ���
    ������������ַ����������Լ��ࡣ����ȫ�����Ƕ��󣬶������Ƕ��Ǵ�һ���ഴ��������

        >>> age = 35
        >>> age.__class__
        <type 'int'>
        >>> name = 'bob'
        >>> name.__class__
        <type 'str'>
        >>> def foo(): pass
        >>>foo.__class__
        <type 'function'>
        >>> class Bar(object): pass
        >>> b = Bar()
        >>> b.__class__
        <class '__main__.Bar'>

    ���ڣ������κ�һ�� __class__ �� __class__ ��������ʲô�أ�

        >>> a.__class__.__class__
        <type 'type'>
        >>> age.__class__.__class__
        <type 'type'>
        >>> foo.__class__.__class__
        <type 'type'>
        >>> b.__class__.__class__
        <type 'type'>

    ��ˣ�Ԫ����Ǵ��������ֶ���Ķ�����
    �����ϲ���Ļ������԰�Ԫ���Ϊ���๤��������Ҫ�͹���������:D��
    type ����Python���ڽ�Ԫ�࣬��Ȼ�ˣ���Ҳ���Դ����Լ���Ԫ�ࡣ

        >>> class Something(object):
        ...     pass
        ...
        >>> Something
        <class '__main__.Something'>
        >>> type(Something)
        <type 'type'>
        >>> type(int) # ˵�� int ������ type ������
        <type 'type'>
        >>> type(type) # ˵�� type ��Ҳ���� type ������
        <type 'type'>


__metaclass__ ����
    �������дһ�����ʱ��Ϊ����� __metaclass__ ���ԡ�

        class Foo(object):
            __metaclass__ = something��
        [��]

    �������ô���ˣ�Python�ͻ���Ԫ����������Foo��С�ĵ㣬��������Щ���ɡ�
    ������д�� class Foo(object)�����������Foo��û�����ڴ��д�����
    Python������Ķ�����Ѱ�� __metaclass__ ���ԣ�����ҵ��ˣ�Python�ͻ�������������Foo�����û���ҵ����ͻ����ڽ��� type ����������ࡣ
    ��������λ����������Ρ�����д���´���ʱ:

        class Foo(Bar):
            pass

    Python�������µĲ�����
    Foo���� __metaclass__ �������������ǣ�Python�����ڴ���ͨ�� __metaclass__ ����һ������ΪFoo���������˵���������������ҵ�˼·����
    ���Pythonû���ҵ� __metaclass__ �����������Bar�����ࣩ��Ѱ�� __metaclass__ ���ԣ�����������ǰ��ͬ���Ĳ�����
    ���Python���κθ����ж��Ҳ��� __metaclass__ �����ͻ���ģ������ȥѰ�� __metaclass__ ����������ͬ���Ĳ�����
    ��������Ҳ��� __metaclass__ ��Python�ͻ������õ� type ��������������

    ���ڵ�������ǣ�������� __metaclass__ �з���Щʲô�����أ��𰸾��ǣ����Դ���һ����Ķ�����
    ��ôʲô������������һ�����أ� type �������κ�ʹ�õ� type �������໯ type �Ķ��������ԡ�


�Զ���Ԫ��
    Ԫ�����ҪĿ�ľ���Ϊ�˵�������ʱ�ܹ��Զ���ظı��ࡣ
    ͨ�������ΪAPI�����������飬��ϣ�����Դ������ϵ�ǰ�����ĵ��ࡣ
    ����һ����ɵ�����ӣ�����������ģ�������е�������Զ�Ӧ���Ǵ�д��ʽ��
    �кü��ַ������԰쵽��������һ�־���ͨ����ģ�鼶���趨 __metaclass__ ��
    �������ַ��������ģ���е������඼��ͨ�����Ԫ��������������ֻ��Ҫ����Ԫ������е����Զ��ĳɴ�д��ʽ�����´��ˡ�

    ���˵��ǣ� __metaclass__ ʵ���Ͽ��Ա�������ã���������Ҫ��һ����ʽ���ࣨ��֪����ĳЩ��������С�class���Ķ���������Ҫ��һ�� class ������ͼ����£�����а�������
    ���ԣ��������������һ���򵥵ĺ�����Ϊ���ӿ�ʼ��

        # Ԫ����Զ�����ͨ��������type���Ĳ�����Ϊ�Լ��Ĳ�������
        def upper_attr(future_class_name, future_class_parents, future_class_attr):
            '''����һ������󣬽����Զ�תΪ��д��ʽ'''

            # ѡ�����в���'__'��ͷ������
            attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))

            # ������תΪ��д��ʽ
            uppercase_attr = dict((name.upper(), value) for name, value in attrs)

            # ͨ��'type'���������Ĵ���
            return type(future_class_name, future_class_parents, uppercase_attr)

        # ������õ����ģ���е�������
        __metaclass__ = upper_attr

        # ע�⣺��������ܼ̳� object �ࡣ
        # ���� __metaclass__ �Ĳ���˳���ȥ���� ����object �� __metaclass__ �� ��ȥ���� ����object ��ģ��� __metaclass__ ���Ǿ͵�����ģ��� __metaclass__ ʧЧ��
        # ���⣬������ py2.6, py2.7 �����������гɹ����� py3.4 ʧ�ܣ�ԭ��δ֪��
        class Foo():

            # ����Ҳ����ֻ�����ﶨ�� __metaclass__ ��������ֻ���������������
            bar = 'bip'

        print( hasattr(Foo, 'bar') ) # ���: False
        print( hasattr(Foo, 'BAR') ) # ���:True

        f = Foo()
        print( f.BAR ) # ���:'bip'


    ��������������һ�Σ���һ����һ�������� class ������Ԫ�ࡣ

        # ���ס��'type'ʵ������һ���࣬����'str'��'int'һ���� ���ԣ�����Դ�type�̳�
        class UpperAttrMetaClass(type):

            # __new__ ���� __init__ ֮ǰ�����õ����ⷽ��
            # __new__ �������������󲢷���֮�ķ���
            # �� __init__ ֻ������������Ĳ�����ʼ��������
            # ������õ� __new__ ��������ϣ���ܹ����ƶ���Ĵ���
            # ��������Ķ������࣬����ϣ���ܹ��Զ��������������������д __new__
            # �����ϣ���Ļ�����Ҳ������ __init__ ����Щ����
            # ����һЩ�߼����÷����漰����д__call__���ⷽ���������������ﲻ��

            def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
                attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
                uppercase_attr = dict((name.upper(), value) for name, value in attrs)
                return type(future_class_name, future_class_parents, uppercase_attr)
                # ��д��ֻ�ܹ������ __metaclass__ ���ã� �������������Ч��


    ���ǣ����ַ�ʽ��ʵ����OOP������ֱ�ӵ����� type ����������û�и�д����� __new__ ��������������������ȥ����:

        class UpperAttrMetaclass(type):
            def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
                attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
                uppercase_attr = dict((name.upper(), value) for name, value in attrs)
                # ����type.__new__����
                # ����ǻ�����OOP��̣�ûʲôħ��
                return type.__new__(upperattr_metaclass, future_class_name, future_class_parents, uppercase_attr)
                # ��д����ʹ������Ҳ����Ч��

    ������Ѿ�ע�⵽���и�����Ĳ��� upperattr_metaclass ���Ⲣû��ʲô�ر�ġ�
    �෽���ĵ�һ���������Ǳ�ʾ��ǰ��ʵ������������ͨ���෽���е� self ����һ����
    ��Ȼ�ˣ�Ϊ������������������������ıȽϳ������Ǿ��� self һ�������еĲ����������ǵĴ�ͳ���ơ�
    ��ˣ�����ʵ�Ĳ�Ʒ������һ��Ԫ��Ӧ�����������ģ�

        class UpperAttrMetaclass(type):
            def __new__(cls, name, bases, dct):
                attrs = ((name, value) for name, value in dct.items() if not name.startswith('__')
                uppercase_attr  = dict((name.upper(), value) for name, value in attrs)
                return type.__new__(cls, name, bases, uppercase_attr)

    ���ʹ�� super �����Ļ������ǻ�����ʹ����ø�����һЩ����Ỻ��̳�
    ���ǵģ������ӵ��Ԫ�࣬��Ԫ��̳У��� type �̳У�

        class UpperAttrMetaclass(type):

            # cls: ��Ҫ�������࣬������self������selfָ�����instance��������clsָ�����class
            # name: ������֣�Ҳ��������ͨ��������.__name__��ȡ�ġ�
            # bases: �����Ԫ��
            # attrs: ���Ե�dict��dict�����ݿ����Ǳ���(�����ԣ���Ҳ�����Ǻ������෽������
            def __new__(cls, name, bases, dct):
                attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
                uppercase_attr = dict((name.upper(), value) for name, value in attrs)
                return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)

    ��������������֮�⣬����Ԫ�����û�б�Ŀ�˵���ˡ�
    ʹ�õ�Ԫ��Ĵ���Ƚϸ��ӣ��ⱳ���ԭ�򵹲�������ΪԪ�౾��������Ϊ��ͨ����ʹ��Ԫ��ȥ��һЩ��ɬ�����飬��������ʡ�����Ƽ̳еȵȡ�
    ȷʵ����Ԫ������Щ���ڰ�ħ�������ر����õģ��������Щ���ӵĶ�������
    ����Ԫ�౾����ԣ�������ʵ�Ǻܼ򵥵ģ�
        1)   ������Ĵ���
        2)   �޸���
        3)   �����޸�֮�����


ΪʲôҪ�� metaclass ������Ǻ���?
    ���� __metaclass__ ���Խ����κοɵ��õĶ�����Ϊ�λ�Ҫʹ�����أ���Ϊ����Ȼʹ�������Ӹ��Ӱ��������кü���ԭ��
        1�� ��ͼ������������������ UpperAttrMetaclass(type) ʱ����֪��������Ҫ����ʲô��
        2�� �����ʹ��OOP��̡�Ԫ����Դ�Ԫ���м̳ж�������д����ķ�����Ԫ������������ʹ��Ԫ�ࡣ
        3�� ����԰Ѵ�����֯�ĸ��á�����ʹ��Ԫ���ʱ��϶���������������ٵ����ּ򵥳�����ͨ��������ԱȽϸ��ӵ����⡣������������ܵ�һ�����л���а�����Ҳ��ʹ�ô���������Ķ���
        4�� �����ʹ�� __new__, __init__ �Լ� __call__ ���������ⷽ���������ܰ��㴦��ͬ�����񡣾���ͨ������԰����еĶ������� __new__ �ﴦ�������Щ�˻��Ǿ����� __init__ �����Щ��
        5�� ��Ŷ���ⶫ���������� metaclass ���϶������࣬��ҪС�ģ�

    ����ΪʲôҪʹ��Ԫ�ࣿ
    ���ڻص����ǵĴ�����������������Ϊʲô���ȥʹ������һ�����׳����һ�ɬ�����ԣ��ðɣ�һ����˵����������ò�������

    ��Ԫ�������ȵ�ħ����99%���û�Ӧ�ø�������Ϊ�˲��ġ�����������������Ƿ���Ҫ�õ�Ԫ�࣬��ô��Ͳ���Ҫ������Щʵ���õ�Ԫ����˶��ǳ������֪��������Ҫ��ʲô�����Ҹ�������Ҫ����ΪʲôҪ��Ԫ�ࡣ��  ���� Python������� Tim Peters

    Ԫ�����Ҫ��;�Ǵ���API��һ�����͵������� Django ORM �������������������壺

        class Person(models.Model):
            name = models.CharField(max_length=30)
            age = models.IntegerField()

    ������������������Ļ���

        guy  = Person(name='bob', age='35')
        print guy.age

    �Ⲣ���᷵��һ�� IntegerField ���󣬶��ǻ᷵��һ�� int ����������ֱ�Ӵ����ݿ���ȡ�����ݡ�
    �����п��ܵģ���Ϊ models.Model ������ __metaclass__ �� ����ʹ����һЩħ���ܹ�����ոն���ļ򵥵�Person��ת��ɶ����ݿ��һ������hook��
    Django��ܽ���Щ�������ܸ��ӵĶ���ͨ����¶��һ���򵥵�ʹ��Ԫ���API���仯��ͨ�����API���´������룬�ڱ�����������Ĺ�����


����
    ���ȣ���֪��������ʵ���ܹ���������ʵ���Ķ���
    �ðɣ���ʵ�ϣ��౾��Ҳ��ʵ������Ȼ��������Ԫ���ʵ����

        >>>class Foo(object): pass
        >>>id(Foo)

    Python�е�һ�ж��Ƕ�������Ҫô�����ʵ����Ҫô��Ԫ���ʵ�������� type ��
    type ʵ���������Լ���Ԫ�࣬�ڴ�Python��������ɲ������ܹ������ģ�����ͨ����ʵ�ֲ���ˣһЩС�ֶ������ġ�
    ��Σ�Ԫ���Ǻܸ��ӵġ����ڷǳ��򵥵��࣬����ܲ�ϣ��ͨ��ʹ��Ԫ�����������޸ġ�
    �����ͨ���������ּ������޸��ࣺ
        1�� Monkey patching
        2)  class decorators

    ������Ҫ��̬�޸���ʱ��99%��ʱ���������ʹ�����������ּ�����
    ��Ȼ�ˣ���ʵ��99%��ʱ����������Ͳ���Ҫ��̬�޸��� :D



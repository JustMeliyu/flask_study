# encoding: utf-8


class MagicMethod(object):
    """各种魔法方法的含义及其使用"""
    # __slots__对实例属性进行限定，只对当前类有效，子类无效，如果子类也定义__slots__，则子类的范围为子类+父类
    __slots__ = ('str_init', 'lll')

    def __new__(cls, *args, **kwargs):
        """真正意义上的构造函数，创建并返回一个实例对象，如果__new__只调用一次，就会得到一个对象
        继承自新式类才有__new__ 这个魔法方法，至少必须要有一个参数cls，代表要实例化的类。
        __new__必须要有返回值，返回实例化出来的实例(很重要)
        """
        print "__new__ be called"
        print id(cls)
        return object.__new__(cls)

    def __init__(self, str_init):
        """实质是调用object.__setattr__() 设置参数，如果重构了 __setattr__() 方法，先执行该方法
        其实是负责初始化操作，相当于一个项目中的配置文件
        """
        # object.__setattr__(self, '_data', {})
        self.str_init = str_init  # 此时会调用__setattr__方法
        self.lll = 11
        # self.aaa = str_init
        # print self._data
        print "01: it is __init__", self.str_init

    def __str__(self):
        """输出函数，在实例对象请求输出的时候会被调用"""
        return "02: it is __str__ %s " % self.str_init

    def __repr__(self):
        """当直接调用实例对象的时候会被调用"""
        print "__repr__ be called"
        return "03: it is __repr__ %s " % self.str_init

    def __getattr__(self, item):
        """尝试访问一个并不存在的属性的时候就会调用"""
        return "04: it is __getattr__ %s " % item

    def __setattr__(self, key, value):
        """设置参数时会调用该方法，相当与设置参数前的一个钩子"""
        if key != 'str_init':
            # self.key = value + "None"                               # 避免循环引用
            # self._data[key] = value + "None"                        # 相当与调用dict 的__setattr__，所以未循环引用
            object.__setattr__(self, key, str(value) + "None")
        else:
            # self._data[key] = value
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        """与__setattr__类似，只有在删除参数的时候才会调用"""
        print "warning, delete param! __delattr__ working"
        return object.__delattr__(self, item)

    def __abs__(self):
        return "abs of str_init %s " % abs(self.str_init)

    # def __getattribute__(self, item):
    #     """会拦截所有属性，包括存在的属性，对于已经存在的属性，会导致该 item=item """
    #     print "item is %s" % item
    #     return item

    def output(self):
        return "output %s " % self.str_init


mm = MagicMethod(-123456)  # 初始化时调用 __init__
# print mm.str_init
# print repr(mm)
print str(mm.str_init)
# print abs(mm)
print "=================="


class A(object):
    pass


class B(A):
    def __init__(self):
        print "__init__被调用"

    def __new__(cls, *args, **kwargs):
        print "__new__被调用"
        print id(cls)
        return object.__new__(A)


b = B()
print b
print type(b)
print id(A)
print id(B)

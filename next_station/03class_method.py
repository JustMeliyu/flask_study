# encoding: utf-8
class MyClass(object):
    def __init__(self):
        self._some_property = "properties are nice"
        self._some_other_property = "VERY nice"

    def normal_method(*args, **kwargs):
        print "calling normal_method({0},{1})".format(args, kwargs)

    @classmethod
    def class_method(*args, **kwargs):
        print "calling class_method({0},{1})".format(args, kwargs)

    @staticmethod
    def static_method(*args, **kwargs):
        print "calling static_method({0},{1})".format(args, kwargs)

    @property
    def some_property(self, *args, **kwargs):
        print "calling some_property getter({0},{1},{2})".format(self, args, kwargs)
        return self._some_property

    @some_property.setter
    def some_property(self, *args, **kwargs):
        print "calling some_property setter({0},{1},{2})".format(self, args, kwargs)
        self._some_property = args[0]

    @property
    def some_other_property(self, *args, **kwargs):
        print "calling some_other_property getter({0},{1},{2})".format(self, args, kwargs)
        return self._some_other_property


o = MyClass()
# 未装饰的方法还是正常的行为方式，需要当前的类实例（self）作为第一个参数。

o.normal_method
# <bound method MyClass.normal_method of <__main__.MyClass instance at 0x7fdd2537ea28>>

o.normal_method()
# normal_method((<__main__.MyClass instance at 0x7fdd2537ea28>,),{})

o.normal_method(1, 2, x=3, y=4)
# normal_method((<__main__.MyClass instance at 0x7fdd2537ea28>, 1, 2),{'y': 4, 'x': 3})

# 类方法的第一个参数永远是该类

o.class_method
# <bound method classobj.class_method of <class __main__.MyClass at 0x7fdd2536a390>>

o.class_method()
# class_method((<class __main__.MyClass at 0x7fdd2536a390>,),{})

o.class_method(1, 2, x=3, y=4)
# class_method((<class __main__.MyClass at 0x7fdd2536a390>, 1, 2),{'y': 4, 'x': 3})

# 静态方法（static method）中除了你调用时传入的参数以外，没有其他的参数。

o.static_method
# <function static_method at 0x7fdd25375848>

o.static_method()
# static_method((),{})

o.static_method(1, 2, x=3, y=4)
# static_method((1, 2),{'y': 4, 'x': 3})

# @property是实现getter和setter方法的一种方式。直接调用它们是错误的。
# “只读”属性可以通过只定义getter方法，不定义setter方法实现。

o.some_property
# 调用some_property的getter(<__main__.MyClass instance at 0x7fb2b70877e8>,(),{})
# 'properties are nice'
# “属性”是很好的功能

o.some_property()
# calling some_property getter(<__main__.MyClass instance at 0x7fb2b70877e8>,(),{})
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object is not callable

o.some_other_property
# calling some_other_property getter(<__main__.MyClass instance at 0x7fb2b70877e8>,(),{})
# 'VERY nice'

# o.some_other_property()
# calling some_other_property getter(<__main__.MyClass instance at 0x7fb2b70877e8>,(),{})
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object is not callable

o.some_property = "groovy"
# calling some_property setter(<__main__.MyClass object at 0x7fb2b7077890>,('groovy',),{})

o.some_property
# calling some_property getter(<__main__.MyClass object at 0x7fb2b7077890>,(),{})
# 'groovy'

o.some_other_property = "very groovy"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: can't set attribute

o.some_other_property
# calling some_other_property getter(<__main__.MyClass object at 0x7fb2b7077890>,(),{})

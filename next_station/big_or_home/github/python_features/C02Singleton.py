# encoding: utf-8
"""
单例模式是一种常用的软件设计模式。在它的核心结构中只包含一个被称为单例类的特殊类。
通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问，从而方便对实例个数的控制并节约系统资源。
如果希望在系统中某个类的对象只能存在一个，单例模式是最好的解决方案

__new__()在__init__()之前被调用，用于生成实例对象。
利用这个方法和类的属性的特点可以实现设计模式的单例模式。单例模式是指创建唯一对象，单例模式设计的类只能实例
"""
from functools import wraps

"""
使用__new__方法
"""


# 在上面的代码中，我们将类的实例和一个类变量 _instance 关联起来，
# 如果 cls._instance 为 None 则创建实例，否则直接返回 cls._instance。
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance


class MyClassNew(Singleton):
    a = 1


print "__new__ singleton"
myclass1 = MyClassNew()
myclass2 = MyClassNew()
print id(myclass1)
print id(myclass2)
"""
使用装饰器
"""


# 们定义了一个装饰器 singleton，它返回了一个内部函数 getinstance，该函数会判断某个类是否在字典 instances 中，
# 如果不存在，则会将 cls 作为 key，cls(*args, **kw) 作为 value 存到 instances 中，否则，直接返回 instances[cls]
def singleton(cls):
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getinstance


@singleton
class MyClassDec(object):
    a = 1


print "decorator singleton"
myclass3 = MyClassDec()
myclass4 = MyClassDec()
print id(myclass3)
print id(myclass4)
"""
使用模块
"""


class MySingleton(object):
    def foo(self):
        pass


my_singleton = MySingleton()
# 在其他文件中使用方式；
# Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，
# 当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。
# 因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了
# from mysingleton import my_singleton
# my_singleton.foo()

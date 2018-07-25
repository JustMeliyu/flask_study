# encoding: utf-8
# 从下面代码可以看出，如果子类继承父类的方法，子类覆盖了父类的静态方法，
# 子类的实例继承了父类的static_method静态方法，调用该方法，还是调用的父类的方法和类属性。
# 子类的实例继承了父类的class_method类方法，调用该方法，调用的是子类的方法和子类的类属性。


class Foo(object):
    X = 1
    Y = 14

    @staticmethod
    def averag(*mixes):  # "父类中的静态方法"
        return sum(mixes) / len(mixes)

    @staticmethod
    def static_method():  # "父类中的静态方法"
        print "父类中的静态方法"
        return Foo.averag(Foo.X, Foo.Y)

    @classmethod
    def class_method(cls):  # 父类中的类方法
        print "父类中的类方法"
        return cls.averag(cls.X, cls.Y)


class Son(Foo):
    X = 3
    Y = 5

    @staticmethod
    def averag(*mixes):  # "子类中重载了父类的静态方法"
        print "子类中重载了父类的静态方法"
        return sum(mixes) / 3


p = Son()
print "result of p.averag(1,5)"
print (p.averag(1, 5))
print "result of p.static_method()"
print (p.static_method())
print "result of p.class_method()"
print (p.class_method())

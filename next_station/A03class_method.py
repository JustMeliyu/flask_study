# encoding: utf-8
"""
实例方法, 静态方法, 类方法区别
    静态方法: 一些具有与类相关的功能方法, 但没有使用类或相关属性. 可以用来设置环境变量, 修改一些类的变量
    类方法:   将类作为第一个参数, 而不是该类的实例.这意味着可以在该方法中使用使用类及其属性, 而不是特定实例;
             用于在初始化类的时候, 数据结构不符合预期, 可以添加额外的处理函数, 然后返回一个初始化的类用于调用类方法
             只需要将类型本身传递给类方法, 因此既可以通过类来调用, 又可以通过实例来调用

实例方法, 静态方法, 类方法继承问题
    从下面代码可以看出,如果子类继承父类的方法,子类覆盖了父类的静态方法,
    子类的实例继承了父类的static_method静态方法,调用该方法,还是调用的父类的方法和类属性.
    子类的实例继承了父类的class_method类方法,调用该方法,调用的是子类的方法和子类的类属性.

类变量
    类变量是可在类的所有实例之间共享的值(也就是说, 它们不是单独分配给每个实例的).
    例如下例中, num_of_instance 就是类变量, 用于跟踪存在着多少个Test 的实例.
    也可以通过实例调用
"""


class Foo(object):
    X = 1
    Y = 14
    num_of_instance = 0

    def __init__(self):
        self.M = 3
        self.N = 11
        Foo.num_of_instance += 1

    def summixes(self):
        return sum([self.M, self.N])

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


print Foo.num_of_instance is Son.num_of_instance
p = Son()
print "result of p.averag(1,5)"
print (p.averag(1, 5))
print "result of p.static_method()"
print (p.static_method())
print "result of p.class_method()"
print (p.class_method())

# 类属性
print "===类属性==="
print Son.num_of_instance  # 输出为1
f1 = Foo()
print Foo.num_of_instance  # 输出为2, 说明其子类在实例化后, 也初始化其父类,
print Son.num_of_instance  # 输出为2
print Foo.num_of_instance is Son.num_of_instance  # 输出为True, 说明两者指向同一个对象


class Person(object):
    name = "aaa"

#
p1 = Person()
p2 = Person()
print p1.name is p2.name
p1.name = "bbb"
# Person.name = 'ccc'
print p1.name  # bbb
print p2.name  # aaa
print Person.name  # aaa

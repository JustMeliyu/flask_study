# coding:utf-8
# 单双下划线区别
# 以单下划线开始的成员变量被称为保护变量, 这种命名方式不能通过 from module import * 导入, 仅供内部使用, 允许本身及子类使用
# 以双下划线开头的, 只能在其类内部使用, 连子类对象也不能访问
# 以双下划线开头与结尾的, 是系统函数, 尽量避免在自己的代码中使用


class A(object):
    def __init__(self):
        self._a = "a"
        self.__b = "b"

    def __method(self):
        print("class A __method")

    def method_x(self):
        print("class A method_x")

    def method(self):
        self.method_x()
        self.__method()


class B(A):
    def __method(self):
        print("class B __method")

    def method_x(self):
        print("class B method_x")

    # def method(self):
    #     self.method_x()
    #     self.__method()


a = A()
a.method()
print a._a
b = B()
b.method()


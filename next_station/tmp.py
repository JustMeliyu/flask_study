print "============================="
class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)
a = A()
a.class_foo(2)
print "=="
print "=="
a.foo(1)
print "=="
A.foo(a, 1)
print "=="
A.static_foo(1)
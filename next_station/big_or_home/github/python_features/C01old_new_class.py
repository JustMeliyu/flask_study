# encoding: utf-8
# 旧式类&深度优先
class A:
    def foo1(self):
        print "A"
class B(A):
    def foo2(self):
        pass
class C(A):
    def foo1(self):
        print "C"
class D(B, C):
    pass


d = D()
d.foo1()    # A

# 新式类&广度优先
class E(object):
    def foo1(self):
        print "A"
class F(E):
    def foo2(self):
        pass
class G(E):
    def foo1(self):
        print "C"
class H(G, F):
    pass


e = E()
e.foo1()

# encoding: utf-8

param_mutable = 1

# 如果传递的是一个可变更对象，是对该对象的引用，如果在函数内部对该对象重新绑定，则在函数外部将不知道它的变更，依然指向原始对象。
def fun(c):
    print "func_in", id(c)  # func_in 41322472
    c = 2
    print "re-point", id(c), id(2)  # re-point 41322448 41322448
print "func_out", id(param_mutable), id(1)  # func_out 41322472 41322472
fun(param_mutable)
print "func_out", id(param_mutable), id(1)  # func_out 41322472 41322472
print param_mutable  # 1


# 可变更对象
print "=========="
param_immutable = []
def fun(b):
    print "func_in", id(b)  # func_in 53629256
    b.append(1)
print "func_out", id(param_immutable)  # func_out 53629256
fun(param_immutable)
print "func_out", id(param_immutable)  # func_out 53629256
print param_immutable  # [1]


# 作用域链
name = "lzl"
def f1():
    # name = "Eric"
    def f2():
        # name = "Snor"
        print(name)
    f2()
    print name
f1()


# 终极版作用域
print "======="
name2 = "lzl"
def f1():
    print(name2)
def f2():
    name2 = "eric"
    f1()
f2()


# lambada 面试题
# 函数在没有执行前，内部代码不执行
li = [lambda: x for x in range(10)]
print(x)
print(li)
# 输出：9
print li[0]()
# print(res)
li1 = [x for x in range(10)]
print li1[0]


def a(param):
    # param = 'b'  # 这里就会出现这样的提示，因为在main定义的param对象被重新指定了新的值
    print param


if __name__ == '__main__':
    param = 'a'
    a(param)

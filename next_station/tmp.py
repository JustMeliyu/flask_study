a = 1

print("out_fun {}".format(id(a)))


def fun1(a):
    print("func_in {}".format(id(a)))
    a = 2
    print("re_point {}, {}".format(id(a), id(2)))


print "func_out", id(a), id(1)
fun1(a)
print a  # 1
print("===========")
a = []


def fun2(a):
    print "func_in", id(a)
    a.append(1)
    print "func_in", id(a)
    a = [1, 2, 3]
    print "func_in", id(a)


print "func_out", id(a)
fun2(a)
print "func_out", id(a)
print a  # [1]

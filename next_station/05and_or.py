# encoding: utf-8
# a = "first"
# b = "second"
a = ""
b = "second"
# 1 and a 是假(a是假)， 假 or b  是b
result1 = 1 and a or b
result2 = 0 and a or b
print "result1 is : ", result1
print "result2 is : ", result2
result3 = (1 and [a] or [b])[0]
result4 = (0 and [a] or [b])[0]
print "result3 is : ", result3
print "result4 is : ", result4
print "============="


# 尽管你不得不使用更复杂的安全形式，也有一些好的理由来使用这个技巧；在Python中有很多时候， if 语句不允许使用
# 可定义函数
def choose(boolvalue, first, second):
    return (boolvalue and [first] or [second])[0]


a = ""
b = "second"
b.split()
qaq = a if 1 else b
aza = a if 0 else b
print qaq
print aza

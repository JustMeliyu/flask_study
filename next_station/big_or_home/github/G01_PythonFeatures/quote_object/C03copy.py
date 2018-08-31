# encoding: utf-8
"""
这里记住的是类型是属于对象的，而不是变量。而对象有两种,“可更改”（mutable）与“不可更改”（immutable）对象。
在python中，strings, tuples, 和numbers是不可更改的对象，而 list, dict, set 等则是可以修改的对象。(这就是这个问题的重点)

列表可以通过引用其元素，改变对象自身(in-place change)。这种对象类型，称为可变数据对象(mutable object)，词典也是这样的数据类型。
而像之前的数字和字符串，不能改变对象本身，只能改变引用的指向，称为不可变数据对象(immutable object)。
我们之前学的元组(tuple)，尽管可以调用引用元素，但不可以赋值，因此不能改变对象自身，所以也算是immutable object.



当一个引用传递给函数的时候,函数自动复制一份引用,这个函数里的引用和外边的引用没有半毛关系了.
所以第一个例子里函数把引用指向了一个不可变对象,当函数返回的时候,外面的引用没半毛感觉.
而第二个例子就不一样了,函数内的引用指向的是可变对象,对它的操作就和定位了指针地址一样,在内存里进行修改.
"""
import copy

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

b = a  # 赋值，传对象的引用
c = copy.copy(a)  # 对象拷贝，浅拷贝。copy仅拷贝对象本身，而不对中的子对象进行拷贝，故对子对象进行修改也会随着修改。
d = copy.deepcopy(a)  # 对象拷贝，深拷贝。deepcopy是真正意义上的复制，即从新开辟一片空间。我们经常说的复制实际上就是deepcopy

a.append(5)  # 修改对象a
a[4].append("c")  # 修改对象a中的['a', 'b']数组对象
print id(a)
print id(b)
print id(c)
print id(d)
print 'a = ', a
print 'b = ', b
print 'c = ', c
print 'd = ', d

e = f = g = [1, 2, [5, 6, 7]]
# g = [1, 2, 3]
g.append(4)
g[2].append(4)
print "e id is {0}, value is : {1}".format(id(e), e)
print "f id is {0}, value is : {1}".format(id(f), f)
print "g id is {0}, value is : {1}".format(id(g), g)
print e is f

# from stackoverflow
# https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
print "===stackoverflow==="
def try_to_change_list_contents(the_list):
    print 'got', the_list
    the_list.append('four')
    print 'changed to', the_list


outer_list = ['one', 'two', 'three']

print 'before, outer_list =', outer_list
try_to_change_list_contents(outer_list)
print 'after, outer_list =', outer_list


# 不可变更对象，我们将一个新的字符串指定给一个新的字符串，但是无法改变outer_string字符串指定的位置。
def try_to_change_string_reference(the_string):
    print 'got', the_string
    the_string = 'In a kingdom by the sea'
    print 'set to', the_string


outer_string = 'It was many and many a year ago'

print 'before, outer_string =', outer_string
try_to_change_string_reference(outer_string)
print 'after, outer_string =', outer_string

# encoding: utf-8

# 这是一个简单的赋值语句，整数 1 为一个对象，a 是一个引用，利用赋值语句，引用a指向了对象1
a = 1
# 你可以通过python的内置函数 id() 来查看对象的身份(identity)，这个所谓的身份其实就是 对象 的内存地址
# python一切皆对象的理念，所以函数也是一个对象，因此可以使用 id() 函数的__doc__方法来查看这个函数的具体描述
print id.__doc__


h = 3
j = 3
print id(h), id(j)
m = 'qsdfdas1324324'
n = 'qsdfdas1324324'
print id(m), id(n)

# 让引用b指向引用a指向的对象
b = a
a = a + 2
print b, a

z = [1, 2, [3, 4]]
print id(z)
print id(z[0])
print id(z[1])
print id(z[2])
z[0] = 0
print id(z[0])  # id 发生变化
z.insert(0, 10)
print id(z[0])
print id(z[1])  # 原z[0]，id 未发生变化


# 赋值可变更对象
li = [1, 2, 3, 4, 5]
li_m = [1, 2, 3]
li[4] = li_m
print li
li_m.append(4)
print li

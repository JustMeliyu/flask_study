# encoding: utf-8
f = open("read.txt")
print f.name
# 读取整个文件
# c_all = f.read()
# print "c_all is : \n", c_all

# readline方法用于从文件读取整行，包括 "\n" 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符
# 读取下一行,使用生成器方法
c_line = f.readline()
c_next = f.next()
print "c_line is : ", c_line.strip()
print "c_next is : ", c_next

# readlines 方法用于读取所有行(直到结束符 EOF)并返回列表,如果碰到结束符 EOF 则返回空字符串。
# 读取整个文件到一个迭代器以供我们遍历
# for line in f.readlines():
#     print line.strip()


f.close()

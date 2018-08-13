# -*- coding:utf-8 -*-

import sys
import os

print "1: ===sys.arvg===\n"
print "argv[0] is : {0}".format(sys.argv[0])
# print sys.argv[1]

print "2: ===sys.path===\n"
# print sys.path
# for p in sys.path:
#     print p

print "3: ===sys.modules===\n"
# print sys.modules
# for k, v in sys.modules.items():
#     print "{0} : {1}".format(k, v)

print "4: ===os与sys的异常推出===\n"
# sys.exit(1)
# try:
#     sys.exit(0)
# except SystemExit:
#     print "process die"
#
#
# print "os module :"
# try:
#     os._exit(0)
# except:
#     print "process die"
print "5: ===os.fork()===\n"
# https://blog.csdn.net/seetheworld518/article/details/49639247
# 子进程永远返回0，而父进程返回子进程ID，这样做的理由是，一个父进程可以fork()出多个子进程。
# 所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID

# pid = os.fork()
# print "current ID is : {0}".format(os.getpid())
# print "pid is {0}".format(pid)
#
# if pid == 0:
#     print "子进程 : {0} , 父进程 : {1}".format(os.getpid(), os.getppid())
# else:
#     print "{0} 构造一个子进程 {1}".format(os.getpid(), pid)

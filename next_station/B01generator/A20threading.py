# encoding:utf-8
import threading
import time


# 定义某个线程要运行的函数
def conuntnum(n):
    print("running on num : {0}\n".format(n))
    time.sleep(3)


if __name__ == "__main__":
    # 生成线程实例
    t1 = threading.Thread(target=conuntnum, args=(23,))
    t2 = threading.Thread(target=conuntnum, args=(34,))

    # 启动线程
    t1.start()
    t2.start()

    print("ending")

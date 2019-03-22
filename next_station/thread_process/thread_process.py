# encoding:utf-8

import threading
import time


def runnn(n):
    print "task {0}\n".format(n)
    # time.sleep(2)
    print '2s {0} \n'.format(n)
    # time.sleep(2)
    print '1s {0} \n'.format(n)
    # time.sleep(2)
    print '0s {0} \n'.format(n)
    # time.sleep(2)


if __name__ == "__main__":
    t1 = threading.Thread(target=runnn, args=("t1111",))
    t2 = threading.Thread(target=runnn, args=("t2222",))
    t1.start()
    t2.start()

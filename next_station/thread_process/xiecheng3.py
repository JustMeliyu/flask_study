# -*-coding:utf-8-*-


def consumer():

    while True:
        n = 0
        r = yield n
        print "===", r
        # if not n:
        #     return
        print('[CONSUMER] Consuming %s...' % r)


def produce(con):
    con.send(None)
    # con.next()
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = con.send(n)
        # r = con.next()
        print('[PRODUCER] Consumer return: %s' % r)
    con.close()


# c = consumer()
# produce(c)
# print c.next()
# print c.next()
# print c.next()
# a = (i for i in xrange(4))
# print a.next()
# print a.next()
# print a.next()


def te():
    for i in range(20):
        n = yield i
        print "===", n

c = te()
# print c
# b = c.send(None)
# print "+++", b
# a = c.send(2)
# print "+++", a
# z = c.send(43)
# print "+++", z
c.send(None)
for i in range(10):
    x = c.send(i + 10)
    print "+++", x


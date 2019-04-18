# encoding: utf-8
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


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


c = consumer()
produce(c)

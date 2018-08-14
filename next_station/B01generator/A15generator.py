# encoding: utf-8
# 生成器
# 当列表数量较大时，而实际需要使用的又只是前面一部分，可使用生成器
# 生成器保存的是算法，每访问一个，计算一个，直到计算到最后一个元素，没有元素时，抛出StopIteration异常
# 可使用next() 依次访问
nn = (m + n for m in "ABC" for n in "XYZ")
print nn
print type(nn)


# for i in nn:
#     print nn.next()
# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00138681965108490cb4c13182e472f8d87830f13be6e88000
# 生成器函数
# 与普通函数不同的地方在于执行流程，普通函数遇到return或函数最后一行完成执行；
# 而生成器函数在每次调用next()的时候执行，遇到yeild返回，再次执行时从上次返回的yield语句处执行；
# 可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。
# 生成器函数的工作原理，是在for循环的过程中，不断的计算出下一个元素，并在适当的条件结束for循环，
# 在python3.3版本之下，不允许在生成器函数中使用return 关键词

# http://python.jobbole.com/87154/
# 没有执行到yield时，则抛出StopIteration异常
# 每次执行迭代器的next()方法并返回后，该方法的上下文环境即消失了，也就是所有在next()方法中定义的局部变量就无法被访问了。
# 而对于生成器，每次执行next()方法后，代码会执行到yield关键字处，并将yield后的参数值返回，同时当前生成器函数的上下文会被保留下来。
# 也就是函数内所有变量的状态会被保留，同时函数代码执行到的位置会被保留，感觉就像函数被暂停了一样。
# 当再一次调用next()方法时，代码会从yield关键字的下一行开始执行。

def fib(max_len):
    index, x, y = 0, 0, 1
    ll = [y]
    while index < max_len:
        yield y
        x, y = y, x + y
        index += 1
        ll.append(y)
    # return ll


for i in fib(10):
    if i < 10:
        print i


def count(n):
    x = 0
    while x < n:
        print "cccc"
        yield x
        # value = yield x
        # print value
        # if value is not None:
        #     print 'Received value: %s' % value
        print "aaaa"
        x += 1
        print "bbbb"


# 我们先调用next()方法，让代码执行到yield关键字（这步必须要），当前打印出0。
# 然后当我们调用”gen.send(‘Hello’)”时，字符串’Hello’就被传入生成器中，并作为yield关键字的执行结果赋给变量”value”，
# 所以控制台会打印出”Received value: Hello”。然后代码继续执行，直到下一次遇到yield关键字后暂定，此时生成器返回的是1。
print "======"
gen = count(5)
print gen.next()  # print 0
print "="
print gen.next()  # print 1
print "="
print gen.send('Hello')  # Received value: Hello, then print 1
print "="

# Python实现协程最简单的方法，就是使用yield。当一个函数在执行过程中被阻塞时，就用yield挂起，然后执行另一个函数。
# 当阻塞结束后，可以用next()或者send()唤醒。相比多线程，协程的好处是它在一个线程内执行，避免线程之间切换带来的额外开销，
# 而且多线程中使用共享资源，往往需要加锁，而协程不需要，因为代码的执行顺序是你完全可以预见的，
# 不存在多个线程同时写某个共享变量而导致出错的情况。


def consumer():
    last = ''
    while True:
        receival = yield last
        if receival is not None:
            print 'Consume %s' % receival
            last = receival


def producer(gen, n):
    gen.next()
    x = 0
    while x < n:
        x += 1
        print 'Produce %s' % x
        last = gen.send(x)

    gen.close()


gen = consumer()
producer(gen, 5)




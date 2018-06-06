from functools import wraps


def f_t1(fun):
    @wraps(fun)
    def f_t2(*args, **kwargs):
        print 12
        fun(*args, **kwargs)
    return f_t2


@f_t1
def f_t3():
    print 34


f_t3()

data = {
    "name": "ly"
}
data2 = ["ly"]
print data2["age"]

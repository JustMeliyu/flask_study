# -*-coding:utf-8-*-
def f(ham: 42, eggs: int = 'spam') -> "Nothing to see here":
    print("函数注释", f.__annotations__)
    print("参数值打印", ham, eggs)
    print(type(ham), type(eggs))


f("rew")

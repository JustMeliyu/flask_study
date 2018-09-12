

def go(i):
    if i == 10:
        return
    i += 1
    go(i)
    print i


go(0)

def a():
    try:
        int(1)
    except:
        return "bb"
    finally:
        print "cc"

a()


collapse = True
processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
s = "this  is\na\ttest"
print "s is : ", s
print "s.split() is : ", s.split()
print "' '.join(s.split) is : ", " ".join(s.split())


def f_1():
    print "f_1"

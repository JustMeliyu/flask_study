i = 1

m = i

print "i is:", i
print "m is:", m
m = 2
print "i is:", i
print "m is:", m
print "========="
d = {}
dt = d
print "d is:", d
print "dt is:", dt
# d = {"a": 1, "b": 2}
d['a'] = 1
d['b'] = 2
print "d is:", d
print "dt is:", dt
print "============"
l_mem = []

l = l_mem  # the first call
for i in range(2):
    l.append(i * i)

print l  # [0, 1]

l = [3, 2, 1]  # the second call
for i in range(3):
    l.append(i * i)

print l  # [3, 2, 1, 0, 1, 4]

l = l_mem  # the third call
print "l is:", l
print "l_men is:", l_mem
for i in range(3):
    l.append(i * i)

print l  # [0, 1, 0, 1, 4]

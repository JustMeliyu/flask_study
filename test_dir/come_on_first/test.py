import re
# re.split()

print "==================="
s = "abc aa;bb,cc | dd(xx).xxx 12.12'	xxxx"
s_s = s.split(" ")
print "str split is : ", s_s

r_s = re.split(r"[ ]", s)
print "re split is : ", re.split(r" ", s)
print "re split is : ", r_s

r_s2 = re.split(r"[\s]", s)

print "re split is : ", r_s2







print "==================="

a = 1234
if not a:
    print "aaaaa"
else:
    print "bbbbbbbb"
b = {
    "aa": 1,
    "bb": 2,
    "cc": 0
}

print b.values()

c = "aaaa"
print int(-1)
print b.get("cc")
print b.get("cc") or b.get("bb")

d = b.get("dd") or 1
print d

if b.get("cc"):
    print b.get("cc")
else:
    print "+++"

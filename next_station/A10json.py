import json

s = '["63","64","2","4","62","5","59","60","55","46","49","52","3"]'
m = json.loads(s)
d = '{"a": 1, "b": 2, "c": 3}'
n = json.loads(d)
print type(m)
print m
print type(n)
print n
print "======"

t = {"a": 1, "b": 2, "c": 3}
tt = json.dumps(t)
print type(tt)
print tt

q = ["63", "64", "2", "4", "62", "5", "59", "60", "55", "46", "49", "52", "3"]
qq = json.dumps(q)
print type(qq)
print qq

# encoding: utf-8

import re
import hashlib



re_date = '\d{4}(-)\d{2}(-)\d{2}$'


def is_date(date_value):
    """判断字符的格式是否为 1990-01-21 """
    return re.match(r'\d{4}(-)\d{2}(-)\d{2}$', str(date_value))


print "===", is_date('AAA1990-12-11')
phone = "2004-959-559 # 这是一个国外电话号码"
num = re.sub(r'#.*$', '', phone)
print "num is :", num
print "phone is :", phone

num2 = re.sub(r'\D', '', phone)
print "num2 is :", num2
print "phone is :", phone

s_m = 'a{5}'

print "s_m: ", re.search(s_m, 'aaaa')

s_m_n = 'a{3,5}'

print "s_m_n: ", re.search(s_m_n, 'aaaaaa')

s_m_n_q = 'a{3,5}?'

print "s_m_n_q: ", re.search(s_m_n_q, 'aaaaaaaaaas')

emailRegex = r"[-_\w\.]{0,64}@([-\w]{1,63}\.)*[-\w]{1,63}"


s_end = r'[0-9]{3, 5}$'

t = re.search(r'\d{3,5}', "asdasda0223sa123")

print "s_end: ", t
print "s_end: ", t.group(0)
# print "s_end: ", t.group(1)
print "s_end: ", t.span(0)
print "s_end: ", re.search(r'[0-9]{3,5}$', "asdasda0223")


print "========================="

my_dict = {"a": 1, "b": 2}
my_set = {1, 2, 3, 3}
print my_set
print type(my_set)
a = set()
# a = {1, 2, 3, 4}

dict_t = {"a": 1, "b": 2, "c": 3}
list_t = [1, 2, 3, 3, 4, 2, 4]
set_t = set(list_t)
print "!!!:", set_t
print "@@@:", set(dict_t)


def ch_l(s_a, required=[]):
    required.append(s_a)
    return required


a = []
print ch_l(1, a)
print ch_l(2, a)


class AsssSss(object):
    pass


print "================="
m = hashlib.md5()
m.update("liyu")
m.update("uyil")
m2 = m.hexdigest()
print m2


m3 = hashlib.md5()
m3.update('liyuuyil')
m4 = m3.hexdigest()
print m4


aa = None
bb = ""
if not aa:
    print(1)
if not bb:
    print(2)
else:
    print(3)
if not aa and not bb:
    print(4)
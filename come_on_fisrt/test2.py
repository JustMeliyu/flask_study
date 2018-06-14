a = {}
# a["q"]
b = []
try:
    b["d"]
    raise KeyError
    print(111)
except:
    print(222)
# a.get("s").strip()
# try:
#     b = a.get("s")
#     b = b.strip()
# except:
#     print(1)
#
# print(b)


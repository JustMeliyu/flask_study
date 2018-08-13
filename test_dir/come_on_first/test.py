import sys

aa = __import__("app.services", {}, {}, ['go_test'])
# print aa.path
# from app import views
bb = getattr(aa, "go_test")
print "bb is : ", bb

print aa
print dir()
print sys.modules["app.services.go_test"]
aa.go_test.g_te()
# aa.article.Articles()
# aa.services.go_test.g_te()
print "+++++++++++"
__import__("g_test")
print sys.modules["g_test"]
print dir()


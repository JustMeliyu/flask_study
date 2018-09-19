import datetime

# expire_time = datetime.date.today() + datetime.timedelta(seconds=7200)


s = datetime.datetime(year=2018, month=9, day=19, hour=11, minute=0)

m = datetime.datetime(year=2018, month=9, day=20, hour=19, minute=30)

q = datetime.datetime(year=2018, month=9, day=19, hour=8, minute=11, second=34)

print q + (m - s)


aa = datetime.datetime(year=2018, month=9, day=19, hour=1, minute=53, second=20)
pp = datetime.timedelta(minutes=953)
bb = datetime.datetime(year=2018, month=9, day=19, hour=9, minute=59, second=59)

print aa - bb
print (aa - bb).seconds
print (aa - bb).seconds / 60
print bb - aa
print (bb - aa).seconds
print (bb - aa).seconds / 60

print bb < aa

print -(bb - aa).seconds / 60

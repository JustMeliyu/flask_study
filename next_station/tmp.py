from celery import Celery
import time
BROKER_URL = "redis://:@localhost:6379/1"
CELERY_RESULT_BACKEND = "redis://:@localhost:6379/2"


app = Celery('tmp', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)
# from tasks import app

x = app.send_task('tasks.add', args=[1, 14], queue="first_task_queue")
n = 1
print x.ready(),
print x.status
print "==="
while x.status == "PENDING":
    time.sleep(1)
    print n,
    print x.ready(),
    print x.status,
    print "\n"
    n += 1
# time.sleep(15)
print "==="
print x.ready()
print x.status
print x.get()

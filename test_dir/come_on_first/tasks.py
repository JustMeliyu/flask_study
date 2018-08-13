from celery import Celery


BROKER_URL = "redis://:127.0.0.1@6379:1"
CELERY_RESULT_BACKEND = "redis://:127.0.0.1@6379:2"

# app = Celery('tasks', broker='amqp://guest@localhost//')
app = Celery('tasks', broker=BROKER_URL)


@app.task
def add(x, y):
    return x + y


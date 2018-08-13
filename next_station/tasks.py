from celery import Celery, Task
from celery.utils.log import get_task_logger
import time
from datetime import timedelta
BROKER_URL = "redis://:@localhost:6379/1"
CELERY_RESULT_BACKEND = "redis://:@localhost:6379/2"


app = Celery('tasks', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)
logger = get_task_logger(__name__)


class MyTask(Task):
    def run(self, *args, **kwargs):
        pass

    def on_success(self, retval, task_id, args, kwargs):
        logger.info('task done: {0}'.format(retval))
        return super(MyTask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.error('task fail, resion: {0}'.format(exc))
        return super(MyTask, self).on_success(exc, task_id, args, kwargs, einfo)


@app.task(base=MyTask, bind=True)
def add(self, x, y):
    time.sleep(10)
    logger.info(self.request.__dict__)
    return "x + y: %d + %d = %d" % (x, y, x + y)


@app.task
def ex():
    execfile('tmp.py')


app.conf.beat_schedule = {
    "10-seconds": {
        "task": "task.ex",
        "schedule": timedelta(seconds=15),
        "args": ()
    }
}


def add_p(x, y):
    return x + y


if __name__ == "__main__":
    print add_p(1, 3)



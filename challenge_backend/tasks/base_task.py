from celery import Task


class BaseTask(Task):
    name = "challenge_backend.base_task"

    def run(self, *args, **kwargs):
        print("debug")

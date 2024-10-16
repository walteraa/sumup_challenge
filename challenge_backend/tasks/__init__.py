from sumup_challenge.celery import app
from challenge_backend.tasks.base_task import BaseTask

app.register_task(BaseTask)

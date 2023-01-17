from celery import Celery


celery_app = Celery(
    "app.celeryworker.worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

# celery_app.conf.task_routes = {"app.worker.test_celery": "main-queue"}

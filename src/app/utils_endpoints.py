from typing import Any

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from celery.result import AsyncResult

from app.core.celery_app import celery_app
# from app.celeryworker.worker import test_celery as t_celery

router = APIRouter()


class Msg(BaseModel):
    msg: str


@router.post("/test-celery/", status_code=201)
def test_celery(
    msg: Msg,
) -> Any:
    task = celery_app.send_task("my_task", args=[msg.msg])
    # task = t_celery.delay(msg.msg)
    return {"msg": "Word received", "task_id": task.id}


@router.get("/tasks/{task_id}")
def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return result

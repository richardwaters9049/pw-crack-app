from celery import Celery
import subprocess
import json


def make_celery():
    celery = Celery(
        "tasks",
        backend="redis://localhost:6379/0",  # Use Redis as the backend
        broker="redis://localhost:6379/0",  # Use Redis as the broker
    )
    return celery


celery = make_celery()


@celery.task(name="tasks.crack_password_task")  # Explicitly set the task name
def crack_password_task(password, method):
    try:
        result = subprocess.run(
            ["python3", "worker.py", password, method],
            capture_output=True,
            text=True,
            timeout=300,  # 5 minutes timeout
        )
        result_json = json.loads(result.stdout)
        return result_json.get("password"), result.returncode == 0
    except subprocess.TimeoutExpired:
        return "Process timed out", False
    except json.JSONDecodeError:
        return "Error decoding result", False

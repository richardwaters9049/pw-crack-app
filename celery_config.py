from celery import Celery


def make_celery(app_name):
    celery = Celery(
        app_name,
        backend="redis://localhost:6379/0",  # Redis backend
        broker="redis://localhost:6379/0",  # Redis broker
    )
    celery.conf.update(
        result_backend="redis://localhost:6379/0",
        broker_url="redis://localhost:6379/0",
    )
    return celery

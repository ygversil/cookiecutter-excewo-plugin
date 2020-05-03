"""Tasks for {{ cookiecutter.package_name }}."""


from celery.utils.log import get_task_logger
from extensible_celery_worker import app


logger = get_task_logger(__name__)


@app.task(bind=True)
def add(self, x, y):
    logger.info('Request {id_}: computing {x} + {y}'.format(
        id_=self.request.id, x=x, y=y
    ))
    return x + y

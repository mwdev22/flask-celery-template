from celery import Celery, shared_task, current_app
import requests
import logging
import os
from app.extensions import LOG_DIR


# logger config
logger = logging.getLogger(__name__)
log_file = os.path.join(LOG_DIR, f'{__name__}.log')
handler = logging.FileHandler(log_file)
formatter = logging.Formatter("%(asctime)s -- %(levelname)s -- %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


@shared_task
def task():
    logger.info('task done')
    return 'task'


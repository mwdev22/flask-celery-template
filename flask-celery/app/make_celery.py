from app import create_app
from celery import Celery

# create an app instance for celery
flask_app = create_app()
app: Celery = flask_app.celery

# discover the shared_task, cant import celery in tasks.py file cause of relative imports
app.autodiscover_tasks()

# celery async automatic task config
app.conf.beat_schedule = {
    
    'run-task-every-5-seconds': {
        # 'task': 'app.tasks.task2',
        # 'schedule': 5.0,  
    },
}


# celery -A app.make_celery worker --loglevel=INFO
# celery -A app.make_celery  beat --loglevel=INFO
from flask_sqlalchemy import SQLAlchemy
from celery import Celery, Task
from flask import Flask
from flask_migrate import Migrate
import os

db = SQLAlchemy() # to be deleted, gonna help in development

# extensions
EXTENSIONS = {
    'db': SQLAlchemy(),
    'migrate': Migrate(),
    'celery': None
}

APPDIR = os.path.dirname(__file__)
ROOTDIR = os.path.dirname(APPDIR)
LOG_DIR = os.path.join(ROOTDIR, 'log')

# celery initialization

# TODO celery config, implementing celery inside app factory
def celery_init_app(app: Flask) -> Celery:
    
    # this ensures that task are going to run with our current app context
    class ContextTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=ContextTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.celery = celery_app
    return celery_app

def init(app):

    EXTENSIONS['db'].init_app(app)
    EXTENSIONS['migrate'].init_app(app, EXTENSIONS['db'], render_as_batch=True)
    EXTENSIONS['celery'] = celery = celery_init_app(app)
    
  

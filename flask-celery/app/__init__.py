from flask import Flask
from app import extensions
import os
import subprocess
from celery import Celery
import logging
import os
from app.extensions import ROOTDIR, APPDIR, LOG_DIR



logger = logging.getLogger(__name__)

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)



log_file = os.path.join(LOG_DIR, f'{__name__}.log')
logging.basicConfig(level=logging.INFO, filename=f'log/{__name__}.log', format="%(asctime)s -- %(levelname)s -- %(message)s")



def create_app(config_file='config.py'):

    
    # base config
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    
    # extensions config
    app.config.from_mapping(
        CELERY=dict(
            broker_url="redis://localhost:6379/0",
            result_backend="redis://localhost:6379/0",
            task_ignore_result=True,
        ),
    )
    extensions.init(app)
    globals().update(extensions.EXTENSIONS)
    
    return app


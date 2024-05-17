import os
from datetime import timedelta
import json

basedir = os.path.abspath(os.path.dirname(__file__))
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, 'db_config.json')
db_config = json.load(open(config_path, 'r'))


# SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{db_config['username']}:{db_config['password']}@{db_config['server']}/{db_config['database']}?driver=ODBC+Driver+17+for+SQL+Server"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)

PERMANENT_SESSION_LIFETIME = timedelta(days=1)
SESSION_TYPE = 'cookie'

DEBUG = False
ENV = 'development'

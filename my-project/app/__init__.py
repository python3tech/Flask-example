# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initilize the app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from . import views

# Load the config file

app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flask_db'
db = SQLAlchemy(app)

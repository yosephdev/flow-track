import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

try:
    import env
except ImportError:
    pass

app = Flask(__name__)

app.config.from_object(Config)

app.config["SQLALCHEMY_DATABASE_URI"] = app.config["SQLALCHEMY_DATABASE_URI"].replace("postgres://", "postgresql://", 1)

db = SQLAlchemy(app)

from . import routes
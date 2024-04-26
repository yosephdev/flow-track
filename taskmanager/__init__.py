import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

uri = app.config["SQLALCHEMY_DATABASE_URI"]
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

from . import routes
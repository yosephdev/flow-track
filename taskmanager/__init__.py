import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

with app.app_context():
    db = SQLAlchemy(app)

from taskmanager import routes
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

with app.app_context():
  db = SQLAlchemy(app)
migrate = Migrate(app, db)

from taskmanager import routes, models
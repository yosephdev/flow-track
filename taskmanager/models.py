from taskmanager import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    """
    User model for storing user information.

    Attributes:
        id (int): Unique identifier for the user.
        username (str): Username of the user (unique, not nullable).
        email (str): Email address of the user (unique, not nullable).
        password (str): Hashed password of the user (not nullable).
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)   
    

class Category(db.Model):
    """
    Represents a category for tasks.

    Attributes:
        id (int): The unique identifier for the category.
        category_name (str): The name of the category (unique and not nullable).
        tasks (list): A list of tasks associated with the category.
    """
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="category", cascade="all, delete, delete-orphan")

    def __repr__(self):
        """Represent the category as a string."""
        return self.category_name


class Task(db.Model):
    """
    Represents a task.

    Attributes:
        id (int): The unique identifier for the task.
        task_name (str): The name of the task (unique and not nullable).
        task_description (str): The description of the task (not nullable).
        is_urgent (bool): Indicates whether the task is urgent (default is False).
        due_date (datetime.datetime): The due date of the task (not nullable).
        category_id (int): The identifier of the category the task belongs to (not nullable).
    """
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        """Represent the task as a string."""
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
from flask import render_template, request, redirect, url_for, flash
from taskmanager import app, db
from taskmanager.models import Category, Task

@app.route("/")
def home():
    tasks = list(Task.query.all())
    return render_template("tasks.html", tasks=tasks)

@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(
            category_name=request.form.get("category_name")
        )
        db.session.add(category)
        db.session.commit()
        flash("Category Added Successfully")
        return redirect(url_for("categories"))
    return render_template("add_category.html")

@app.route("/tasks")
def tasks():
    tasks = list(Task.query.order_by(Task.due_date).all())
    return render_template("tasks.html", tasks=tasks)

@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id")
        )
        db.session.add(task)
        db.session.commit()
        flash("Task Added Successfully")
        return redirect(url_for("tasks"))
    return render_template("add_task.html", categories=categories)
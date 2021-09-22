from flask import Flask, render_template
from flask import Blueprint
from repositories import task_repository

tasks_blueprint = Blueprint("tasks", __name__)

# Index..
# GET '/tasks/'

@tasks_blueprint.route("/tasks/")
def tasks():
    tasks = task_repository.select_all()
    return render_template("tasks/index.html", all_tasks = tasks)

# NEW
# GET '/tasks/new'
# Returns an HTML form to the browser..

@tasks_blueprint.route("/tasks/new/", methods=['GET'])
def new_task():
    return render_template("tasks/new.html")

# CREATE
# POST '/tasks/'
# Receives the data from the form to insert into the database..

# SHOW
# GET '/tasks/<id>'

# EDIT
# GET '/tasks/<id>/edit'

# UPDATE
# PUT '/tasks/<id>'

# DELETE
# DELETE '/tasks/<id>'
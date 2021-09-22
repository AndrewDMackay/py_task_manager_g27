from db.run_sql import run_sql

from models.task import Task
from models.user import User
import repositories.user_repository as user_repository


def save(task):
    sql = "INSERT INTO tasks (description, user_id, duration, completed) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [task.description, task.user.id, task.duration, task.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    task.id = id
    return task


def select_all():
    tasks = []

    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        task = Task(row['description'], user, row['duration'], row['completed'], row['id'] )
        tasks.append(task)
    return tasks



def select(id):
    task = None
    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = user_repository.select(result['user_id'])
        task = Task(result['description'], user, result['duration'], result['completed'], result['id'] )
    return task


def delete_all():
    sql = "DELETE  FROM tasks"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM tasks WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(task):
    sql = "UPDATE tasks SET (description, user_id, duration, completed) = (%s, %s, %s, %s) WHERE id = %s"
    values = [task.description, task.user.id, task.duration, task.completed, task.id]
    run_sql(sql, values)

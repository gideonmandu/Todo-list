from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from bson import ObjectId

from todolist.auth import signin_required
from todolist import db

bp = Blueprint("tasks", __name__)


@bp.route("/")
def index():
    """Show all the task notes, most recent first."""
    tasks_col = db.get_tasks()
    tasks = tasks_col["tasks"].find({})[0]['Tasks']

    return render_template("tasks/index.html", tasks=tasks)

def get_task(id, check_author=True):
    """Get a task and its author by id.
    Checks that the id exists and optionally that the current user is
    the author.
    :param id: id of task to get
    :param check_author: require the current user to be the author
    :return: the task with author information
    :raise 404: if a task with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    task = db.get_tasks().find({
        '_id': ObjectId(id)
        })[0]

    if task is None:
        abort(404, "task id {0} doesn't exist.".format(id))

    if check_author and task["User_id"] != ObjectId(g.user["id"]):
        abort(403)

    return task['Tasks'][0]['Task']


@bp.route("/create", methods=("GET", "POST"))
@signin_required
def create():
    """Create a new task for the current user."""
    if request.method == "POST":
        title = request.form["title"]
        task = request.form["task"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            tasks = db.get_tasks()
            tasks['tasks'].insert_one({
                'Title': title,
                'Tasks': { 
                    'Task': task,
                    'TaskState': False
                },
                'User_id': ObjectId(g.user['id'])
            })
            return redirect(url_for("tasks.index"))

    return render_template("tasks/create.html")


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@signin_required
def update(id):
    """Update a task if the current user is the author."""
    task = get_task(id)

    if request.method == "POST":
        title = request.form["title"]
        task = request.form["task"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            tasks = db.get_tasks()
            tasks['tasks'].update_one(
                {'User_id': ObjectId(id)},

                )
            return redirect(url_for("tasks.index"))

    return render_template("tasks/update.html", task=task)


@bp.route("/<int:id>/delete", methods=("tasks",))
@signin_required
def delete(id):
    """Delete a task.
    Ensures that the task exists and that the logged in user is the
    author of the task.
    """
    tasks = db.get_tasks()
    tasks.delete_one({'_id': ObjectId(id)})
    # db.execute("DELETE FROM tasks WHERE id = ?", (id,))
    # db.commit()
    return redirect(url_for("tasks.index"))
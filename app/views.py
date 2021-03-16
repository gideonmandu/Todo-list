from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask import Blueprint
from flask import flash
from flask import session
from flask import g
from datetime import datetime
from bson import ObjectId
from werkzeug.exceptions import abort

from .db import tasks
from .auth import signin_required

bp = Blueprint('tasks', __name__)


def get_post(id, check_author=True):
    """Get a post and its author by id.
    Checks that the id exists and optionally that the current user is
    the author.
    :param id: id of post to get
    :param check_author: require the current user to be the author
    :return: the post with author information
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    task = tasks.find_one({'User_id': id})

    if task is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and task[0]["User_id"] != g.user["id"]:
        abort(403)

    return task


@bp.route('/')
def index():
    if 'user_id' in session:
        db_tasks = tasks.find({'User_id': session['user_id']})
        disp_tasks = []
        for task in db_tasks:
            # print(task)
            # print(task['Title'])
            # print(task['Tasks'][0]['Task'])
            # print(task['Tasks'][0]['Created'])
            # print(task['Tasks'][0]['Status'])
            disp_tasks.append(task)

        user = session['user_id']
        return render_template('views/index.html', disp_tasks=disp_tasks, user=user)
    else:
        error = 'Sign in Or Sign Up to use the application'
        flash(error)
        return render_template('views/index.html')


@bp.route("/create", methods=("GET", "POST"))
@signin_required
def create():
    """Create a new task for the current user."""
    if request.method == "POST":
        title = request.form["title"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            task = request.form["task"]
            # print(session[0][])
            tasks.insert_one({
                'Title': title,
                'User_id': session['user_id'],
                'Tasks': [
                    {
                        'Task': task, 'Status': False,
                        'Updated': None, 'Created': datetime.utcnow()
                    }
                ]
            })
            return redirect(url_for('index'))

    return render_template("views/create.html")


@bp.route("/update/<string:id>", methods=("GET", "POST"))
@signin_required
def update(id):
    """Update a post if the current user is the author."""
    # task = tasks.find({})[0]['_id']
    print(id)
    query = {'_id': ObjectId(id)}
    # db_task = tasks.find_one(query)[0]
    db_task = tasks.find_one(query)
    print(db_task)
    cd=db_task['Tasks'][0]['Created']
    print(cd)

    if request.method == "POST":
        # title = request.values.get["title"]
        title = request.form['title']
        error = None
        # print('title')ObjectObject

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            # task = request.values.get["task"]
            task = request.form['task']
            radio = request.values.get('status')
            #If radio is 'True' status is True
            status = radio == 'True'
            print(status)
            tasks.update(
                query,
                {
                    '$set': {
                        'Title': title,
                        'Tasks': [
                            {
                                'Task': task,
                                'Status': status,
                                'Updated': datetime.utcnow(),
                                'Created': cd
                            }
                        ]
                    }
                }
            )
            print(f'Task{id} Updated')
            return redirect(url_for("tasks.index"))

    # return render_template("views/update.html", task=task)
    return render_template("views/update.html", db_task=db_task)


@bp.route("/delete/<string:id>", methods=("POST","GET"))
@signin_required
def delete(id):
    """Delete a post.
    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    # task_id = request.values.get(id)
    query = {'_id': ObjectId(id)}
    tasks.delete_one(
        query
    )
    return redirect(url_for("tasks.index"))

from . import init_db
from . import bp
from flask import render_template
from flask import request
from flask import url_for

user_notes = init_db('todo_notes')

@bp.route('/')
def home():
    """
    Loads up app home
    """
    tasks = request.get_json()
    if tasks['status'] == 200:
        pass
    return render_template('views/home/home.html')
    # return 'Hello world'
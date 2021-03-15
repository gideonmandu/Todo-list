import functools
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask import Blueprint
from flask import flash
from flask import session
from flask import g
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from .db import users

bp = Blueprint('auth', __name__, url_prefix='/auth')


def signin_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.signin"))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")

    g.user = None if user_id is None else users.find_one({'Username': user_id})


@bp.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        username = request.form['username']
        passwd = request.form['password']

        if username is None:
            error = 'Please input Username'
            return redirect(url_for('auth.signup'))

        elif passwd is None:
            error = 'Please input Password'
            return redirect(url_for('auth.signup'))

        elif users.find_one({'Username': username}) is None:
            hashed_pw = generate_password_hash(passwd.encode('utf8'))

            users.insert_one({
                'Username': username,
                'Password': hashed_pw
            }
            )
            error = f'{username} registered.'
            return redirect(url_for('auth.signin'))
        else:
            error = f'Name {username} is already registered.'
            return redirect(url_for('auth.signup'))

        flash(error)

    return render_template('auth/signup.html')


@bp.route('/signin', methods=('GET', 'POST'))
def signin():
    if request.method == 'POST':
        username = request.form['username']
        passwd = request.form['password']

        if username is None:
            error = 'Please input Username'
            return redirect(url_for('auth.signin'))

        elif passwd is None:
            error = 'Enter Password'
            return redirect(url_for('auth.signin'))

        elif users.find_one({'Username': username}) is None:
            error = ' Not Registered'
            return redirect(url_for('auth.signup'))

        else:
            user = users.find_one({'Username': username})
            # print(user)
            db_passwd = user['Password']

            if check_password_hash(db_passwd, passwd.encode('utf8')):
                error = f'User {username} logged In'
                session.clear()
                session['user_id'] = user['Username']
                return redirect(url_for('index'))
            else:
                error = 'Incorrect Password or Username'
                return redirect(url_for('auth.signin'))

        flash(error)

    return render_template('auth/signin.html')


@bp.route("/signout")
def signout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for('index'))

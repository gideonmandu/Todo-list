import functools
from flask import (Blueprint, request, render_template, 
                    flash, g, session, redirect, url_for)
from bson import ObjectId

# Import the database object from the main app module
from ..db.database import init_db
users = init_db('users')

from ..routes import url

# Define the blueprint: 'auth', set its url prefix: app.url/auth
bp = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods
@bp.route('/signin', methods=('GET', 'POST'))
def signin():
    # If sign in form is submitted
    if request.method == 'POST':
        user_n = request.form('username')
        email= request.form('email')
        passwd = request.form('password')
        req = {
            'username': user_n,
            'email': email,
            'password': passwd
        }
        print(req)

        resp = request.get_json()

        if resp['status'] == 200:
            user = users.find({'email': email})

            session['user_id'] = user[0]['_id']

            flash(f'Welcome {user[0]["Username"]}' )

            return redirect(url_for('tasks.home'))

        flash('Wrong email or password', 'error-message')

    return render_template("auth/signin.html")

@bp.route('/signup', methods=('GET', 'POST'))
def signup():
    """
    Registers a user
    """
    if request.method == 'POST':
        user_n = request.form('username')
        email= request.form('email')
        passwd = request.form('password')
        req = {
            'username': user_n,
            'email': email,
            'password': passwd
        }
        print(req)

        resp = request.get_json()

        if resp.status == 200:
            user = users.find({'email': email})

            session['user_id'] = user[0]['_id']

            flash(f'Welcome {user[0]["Username"]}' )

            return redirect(url_for('auth.signin'))

        flash('Wrong email or password', 'error-message')

    return render_template("auth/signup.html")
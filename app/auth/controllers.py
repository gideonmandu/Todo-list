import functools
from flask import (Blueprint, request, render_template, 
                    flash, g, session, redirect, url_for)
from bson import ObjectId
# from werkzeug.security import check_password_hash
# from werkzeug.security import generate_password_hash

# Import the database object from the main app module
from ..db.database import init_db
users = init_db('users')

from ..routes import url

# Define the blueprint: 'auth', set its url prefix: app.url/auth
bp = Blueprint('auth', __name__, url_prefix='/auth')

# def process_data(posted_data):
#     """
#     gets individual data from json 
#     """
#     username = posted_data['username']
#     passwd = posted_data['password']

#     # creating password level security
#     hashed_pw = generate_password_hash(passwd.encode('utf8'))
#     return [username, hashed_pw]

# def verify_pw(username, passwd):
#     hashed_pw = users.find({'Username': username})[0]['Password']
#     if check_password_hash(hashed_pw, passwd.encode('utf8')):
#         return True
#     else:
#         return False

# def user_task_ids(username):
#     ids = users.find({'Username': username})[0]['Task Ids'][0]#[id]
#     return ids

@bp.route('/signup', methods=('GET', 'POST'))
def signup():
    """
    Registers a user
    """
    if request.method == 'POST':
        user_n = request.form('username')
        passwd = request.form('password')

        # req = {
        #     'username': user_n,
        #     'password': passwd
        # }

        # user = posted_data(req)

        if users.find_one({'Username': user_n}) is None:
            users.insert_one({
                'Username': user[0],
                'Password': user[1],
                'Task_Title_Ids': []
            })
            resp = request.get_json()
            print(resp)
            flash(f'{user_n} has been successfully registered', 'error-message')
            return redirect(url_for('auth.signin'))

    else:
        return redirect(url_for('auth.signup'))

    return render_template("auth/signup.html")

# Set the route and accepted methods
@bp.route('/signin', methods=('GET', 'POST'))
def signin():
    # If sign in form is submitted
    if request.method == 'POST':
        user_n = request.form('username')
        passwd = request.form('password')

        

        # if resp['status'] == 200:
        #     user = users.find({'email': email})

        #     session['user_id'] = user[0]['_id']

        #     flash(f'Welcome {user[0]["Username"]}' )

        #     return redirect(url_for('tasks.home'))

        flash('Wrong email or password', 'error-message')

    return render_template("auth/signin.html")

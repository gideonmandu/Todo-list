import functools
# Import flask dependencies
from flask import (Blueprint, request, render_template, 
                    flash, g, session, redirect, url_for)
import request

# Import password / encryption helper tools
# from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app.db import users

# Import module forms
from app.auth.forms import LoginForm

# Import module models (i.e. User)
# Import url for api requests
# from app.auth.models import User
from app.routes import url

# Define the blueprint: 'auth', set its url prefix: app.url/auth
bp = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods
@bp.route('/signin/', methods=['GET', 'POST'])
def signin():

    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        email= form.email.data
        passwd = form.password.data
        req = {
            'username':'',
            'email': email,
            'password': passwd
        }

        resp = request.post(f'{url}/auth/signin', params=req)

        if resp.status == 200:
            
            user = users.find({'email': email})

                session['user_id'] = user.[0]['_id']

                flash(f'Welcome {user[0]["Username"]}' )

                return redirect(url_for('auth.home'))

        flash('Wrong email or password', 'error-message')

    return render_template("auth/signin.html", form=form)
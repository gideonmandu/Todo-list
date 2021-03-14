import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from bson import ObjectId

from todolist import db

bp = Blueprint("auth", __name__, url_prefix="/auth")


def signin_required(view):
    """View decorator that redirects anonymous users to the signin page."""

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

    if user_id is None:
        g.user = None
    else:
        users = db.get_users()
        g.user = users.find({'_id': ObjectId(user_id)})


@bp.route("/signup", methods=("GET", "POST"))
def signup():
    """Signup a new user.
    Validates that the username is not already taken. Hashes the
    password for security.
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users = db.get_users()
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
            print(users.find({'username': username})[0]['username'])
        elif users.find({'username': username}) == username:
            error = f"User {users.find({'username': username})} is already Signed Up."

        if error is None:
            # the name is available, store it in the database and go to
            # the signin page
            users.insert_one(
                {'username': username}, 
                {'password':generate_password_hash(password)}
            )
            return redirect(url_for("auth.signin"))

        flash(error)

    return render_template("auth/signup.html")


@bp.route("/signin", methods=("GET", "POST"))
def signin():
    """Log in a Registered user by adding the user id to the session."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users = db.get_users()
        error = None
        user = users.find_one({'username': username})

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user[0]["password"], password):
            error = "Incorrect password."

        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session["user_id"] = user["_id"]
            return redirect(url_for("index"))

        flash(error)

    return render_template("auth/signin.html")


@bp.route("/signout")
def signout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("index"))

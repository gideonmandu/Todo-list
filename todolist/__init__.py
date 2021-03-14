import os

from flask import Flask


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        # DATABASE=os.path.join(app.instance_path, "todolist.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    # register the database commands
    from todolist import db

    # db.init_app(app)

    # apply the blueprints to the app
    from todolist import auth, tasks

    app.register_blueprint(auth.bp)
    app.register_blueprint(tasks.bp)

    # make url_for('index') == url_for('tasks.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the tasks blueprint a url_prefix, but for
    # the tutorial the tasks will be the main index
    app.add_url_rule("/", endpoint="index")

    return app


# from flask import Flask, url_for, request
# from markupsafe import escape

# app = Flask(__name__)

# @app.route('/')
# def index():
#     """
#     docstring
#     """
#     return 'index page'

# @app.route('/hello')
# def hello():
#     """
#     docstring
#     """
#     return 'hello, world!'

# @app.route('/login')
# def login():
#     """
#     docstring
#     """
#     return 'logged in!'

# @app.route('/user/<string:username>')
# def profile(username):
#     """
#     docstring
#     """
#     return f'{escape(username)}\'s profile'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

# # with app.test_request_context():
# #     print(url_for('hello'))
# #     print(url_for('login'))
# #     print(url_for('login', next='/'))
# #     print(url_for('profile', username='Mary Jane'))
#     # print(url_for(''))

# with app.test_request_context('/hello', method='POST'):
#     # now you can do something with the request until the
#     # end of the with block, such as basic assertions:
#     assert request.path == '/hello'
#     assert request.method == 'POST'
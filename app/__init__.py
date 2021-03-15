#!/usr/bin/python3

from flask import Flask
import os
print("give me a bottle of rum!")


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev"
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

    # apply the blueprints to the app
    from app import auth, views

    app.register_blueprint(auth.bp)
    app.register_blueprint(views.bp)

    # make url_for('index') == url_for('tasks.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the tasks blueprint a url_prefix, but for
    # the tutorial the tasks will be the main index
    app.add_url_rule("/", endpoint="index")

    return app

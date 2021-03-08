"""Start with that one in Flask, then we'll got through it. User should be able to Add new to-do note, delete note, update note. Also user should be able to mark note as complete"""

from flask import Flask, render_template, jsonify, request
# Import API
from flask_restful import Api, Resource

# Configurations
from config import config_by_name

# Define the WSGI application object
app = Flask(__name__)
api = Api(app=app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from .auth.controllers import  bp as auth_module
from .views.controllers import bp as tasks_module

# Register blueprint(s)
app.register_blueprint(auth_module)
app.register_blueprint(tasks_module)

# make url_for('home') == url_for('tasks.home')
# in another app, you might define a separate main index here with
# app.route, while giving the tasks blueprint a url_prefix, but for
# the tutorial the blog will be the main index
app.add_url_rule("/", endpoint="home")
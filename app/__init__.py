# Import flask and template operators
"""Start with that one in Flask, then we'll got through it. User should be able to Add new to-do note, delete note, update note. Also user should be able to mark note as complete"""

from flask import Flask, render_template, jsonify, request
# Import API
from flask_restful import Api, Resource

# Configurations
from config import config_by_name

# Define the WSGI application object
app = Flask(__name__)
api = Api(app)

# Define the database options which is imported
# by modules and controllers
from pymongo import MongoClient
def db_init(name):
    client = MongoClient(
    host= config_by_name[name].DB_HOST, 
    port= config_by_name[name].DB_PORT,
    document_class= config_by_name[name].DOC_CLASS,
    tz_aware=config_by_name[name].TZ_AWARE,
    connect=config_by_name[name].CON
    )
    return client

client = db_init('dev')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
# from app.auth.controllers import  mod_auth as auth_module

# Register blueprint(s)
# app.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file
db = client.todo_list

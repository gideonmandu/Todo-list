# Import flask and template operators
"""Start with that one in Flask, then we'll got through it. User should be able to Add new to-do note, delete note, update note. Also user should be able to mark note as complete"""

from flask import Flask, render_template, jsonify, request
# Import API
from flask_restful import Api, Resource

# Define the WSGI application object
app = Flask(__name__)
api = Api(app)

# Configurations
from config import DevelopmentConfig as dev
app.config.from_object('DevelopmentConfig')

# Define the database options which is imported
# by modules and controllers
from pymongo import MongoClient
client = MongoClient(
    host= dev.DB_HOST, 
    port= dev.DB_PORT,
    document_class= dev.DOC_CLASS,
    tz_aware=dev.TZ_AWARE,
    connect=dev.CON
    )

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

# import sqlite3
from pymongo import MongoClient 

import click
from flask import current_app
from flask import g
from flask.cli import with_appcontext

client = MongoClient('mongodb://localhost:27017')
db = client.todolist

# def get_db():
#     """Connect to the application's configured database. The connection
#     is unique for each request and will be reused if this is called
#     again.
#     """

def get_users():
    users = db['users']
    return users

def get_tasks():
    tasks = db['tasks']
    return tasks


# def close_db(e=None):
#     """If this request connected to the database, close the
#     connection.
#     """


# def init_db():
#     """Clear existing data and create new tables."""

# @click.command("init_db")
# @with_appcontext
# def init_db_command():
#     """Clear existing data and create new tables."""


# def init_app(app):
#     """Register database functions with the Flask app. This is called by
#     the application factory.
#     """
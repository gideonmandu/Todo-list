from pymongo import MongoClient
# from flask_pymongo import PyMongo

client = MongoClient()
db = client.todoapp

users = db['users']
tasks = db['tasks']

# app.config['MONGO_URI'] = 'mongodb://localhost:27017/todoapp'
# mongo = PyMongo(app)

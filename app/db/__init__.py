from app import db

user_notes = db['todo_notes']
users = db['users']

from pymongo.collection import Collection
from bson.son import SON

# Import the database object (db) from the main application module
from app.db import users

# Define a User model
# class User():
#     # User Name
#     user = users.find({'Username': username})
#     name = user[0]['Username']

#     # Identification Data: email & password
#     email    = user[0]['email']
#     password = user[0]['Password']
    
#     # Authorisation Data: role & status
#     # role     = db.Column(db.SmallInteger, nullable=False)
#     # status   = db.Column(db.SmallInteger, nullable=False)

#     # New instance instantiation procedure
#     def __init__(self, name, email, password):

#         self.name     = name
#         self.email    = email
#         self.password = password

#     def __repr__(self):
#         return '<User %r>' % (self.name) 
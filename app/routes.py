from app import api
from app.db.add import Add
from app.db.get import Get
from app.db.update import Update
from app.db.delete import Delete
from app.db.users import Signup

api.add_resource(Add, '/add')
api.add_resource(Get, '/get')
api.add_resource(Update, '/update')
api.add_resource(Delete, '/delete')
api.add_resource(Signup,'/signup')

url = 'http://127.0.0.1'
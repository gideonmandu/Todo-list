from app import api
from app.db.add_to_db import Add
from app.db.get_from_db import Get
from app.db.update_db import Update
from app.db.delete_from_db import Delete
# from app.db.user_to_db

api.add_resource(Add, '/add')
api.add_resource(Get, '/get')
api.add_resource(Update, '/update')
api.add_resource(Delete, '/delete')
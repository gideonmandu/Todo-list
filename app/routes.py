from app import api
from .db import Add
from .db import Get
from .db import Update
from .db import Delete
from .db import Signup
from .db import Signin

api.add_resource(Add, '/tasks/add')
api.add_resource(Get, '/tasks/home')
api.add_resource(Update, '/tasks/update')
api.add_resource(Delete, '/tasks/delete')
api.add_resource(Signup,'/auth/signup')
api.add_resource(Signin,'/auth/signin')

url = 'http://127.0.0.1'
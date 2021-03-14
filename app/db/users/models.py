from flask import request
from flask import jsonify
from flask_restful import Resource
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from ..database import init_db
users = init_db('users')

def process_data(posted_data):
    """
    gets individual data from json 
    """
    username = posted_data['username']
    passwd = posted_data['password']

    # creating password level security
    hashed_pw = generate_password_hash(passwd.encode('utf8'))
    return [username, hashed_pw]

def verify_pw(username, passwd):
    hashed_pw = users.find({'Username': username})[0]['Password']
    if check_password_hash(hashed_pw, passwd.encode('utf8')):
        return True
    else:
        return False

def user_task_ids(username):
    ids = users.find({'Username': username})[0]['Task Ids'][0]#[id]
    return ids

class Signup(Resource):
    def post(self):
        # Get data
        if request.method == 'POST':
            # Get posted data from user
            # posted_data = request.get_json()
            # print(request.form('username'))
            # user_n = request.form('username')
            # passwd = request.form('password')
            # req = {
            #     'username': user_n,
            #     'password': passwd
            # }
            # user = process_data(req)
            # # Store username and pw in db
            # users.insert_one({
            #     'Username': user[0],
            #     'Password': user[1],
            #     'Task_Title_Ids': []
            # })

            ret_json = {
                'status': 200,
                'message':'You successfully signed up.'
            }
        else:
            ret_json = {
                'status': 406,
                'message': 'could not access database'
            }
        # return jsonify(ret_json)

class Signin(Resource):
    def post(self):
        # Get posted data from user
        if request.method == 'POST':
            user_n = request.form('username')
            # email= request.form('email')
            passwd = request.form('password')
            req = {
                'username': user_n,
                # 'email': email,
                'password': passwd
            }
        # posted_data = request.get_json()
        # Get data
        # user = process_data(posted_data)

        # Verify user
        correct_pw = verify_pw(user_n, passwd)

        if not correct_pw:
            ret_json = {
                'status':409, #request conflict
                'message': 'Wrong password'
            }
        else:
            ret_json = {
                'status': 200,
                'message':'User password is correct.'
            }
        return jsonify(ret_json)
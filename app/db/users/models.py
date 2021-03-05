from app import Resource, request, jsonify
from app.db import users
import bcrypt

def process_data(posted_data):
    """
    gets individual data from json 
    """
    username = posted_data['username']
    email = posted_data['email']
    passwd = posted_data['password']

    # creating password level security
    hashed_pw = bcrypt.hashpw(passwd.encode('utf8'), bcrypt.getsalt())
    return [username, email, hashed_pw]

def verify_pw(email, passwd):
    hashed_pw = users.find({'Email': email})[0]['Password']
    if bcrypt.hashpw(passwd.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False

def user_task_ids(username):
    ids = users.find({'Username': username})[0]['Task Ids'][0]#[id]
    return ids

class Signup(Resource):
    def post(self):
        # Get posted data from user
        posted_data = request.get_json()
        # Get data
        user = process_data(posted_data)
        # Store username and pw in db
        users.insert_one({
            'Username': user[0],
            'Email': user[1],
            'Password': user[2],
            'Task_Title_Ids': []
        })

        ret_json = {
            'status': 200,
            'message':'You successfully signed up.'
        }
        return jsonify(ret_json)

class Signin(Resource):
    def post(self):
        # Get posted data from user
        posted_data = request.get_json()
        # Get data
        user = process_data(posted_data)

        # Verify user
        correct_pw = verify_pw(user[1], user[2])

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
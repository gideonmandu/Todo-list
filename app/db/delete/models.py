from flask import request
from flask import jsonify
from flask_restful import Resource

from ..database import init_db
tasks = init_db('user_tasks')

class Delete(Resource):
    """
    User Deletes to-do note
    """

    def post(self):
        """
        Delete user task
        """
        # Get user input
        note = request.get_json()

        title = note['title']  # string
        task = note['task']  # string

        # search for note in DB then deletes
        try:
            tasks.find_one_and_delete({'Title': title}, {'Tasks':''})

            # Responce
            resp = {
                # ideally use if request.status_code==200
                'status': 200,
                'message': f'Task {task} in {title} deleted!!!'
            }
        except IndexError:
            print(f'No task with {title} in db')
            # Responce
            resp = {
                'status': 404,
                'error msg': f'No task with {title} in db'
            }
        
        return jsonify(resp)
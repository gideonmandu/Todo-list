from flask import request
from flask import jsonify
from flask_restful import Resource

from ..database import init_db
tasks = init_db('user_tasks')

class Get(Resource):
    """
    User Obtains to-do note
    """

    def post(self):
        """
        Gets user tasks
        """
        # Get user input
        note = request.get_json()

        title = note['title']  # string

        # search for note in DB
        try:
            db_tasks = tasks.find({'Title': title})

            # Responce
            resp = {
                'status': 200,
                'task title': f'{db_tasks[0]["Title"]}',
                'Task':f'{db_tasks[0]["Tasks"][0]["task_1"]}'
            }


        except IndexError:
            print(f'No task with {title} in db')
            # Responce
            resp = {
                'status': 404,
                'error msg': f'No task with {title} in db'
            }

        return jsonify(resp)
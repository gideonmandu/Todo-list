from flask import request
from flask import jsonify
from flask_restful import Resource

from ..database import init_db
tasks = init_db('user_tasks')

class Update(Resource):
    """
    User updates to-do note
    """

    def post(self):
        """
        Updates DB
        """
        # Get user input
        note = request.get_json()

        title = note['title']
        updated_title = note['new title']
        updated_task = note['task']  # string
        updated_task_status = note['status']  # boolean

        # search for note in DB then update
        try:
            db_title = tasks.find({'Title': title})[0]['Title']

            if title == db_title:
                tasks.update_many(
                    {'Title': title},
                    {'$set': {
                        'Title': updated_title,
                        'Tasks.$[elem].task_1': updated_todo,
                        'Tasks.$[elem].task1_status': updated_task_status
                    }, #{array_filters=}
                    }
                )
                # Responce
                resp = {
                    'status': 200,
                    'task': f'Task Updated'
                }
        except IndexError:
            print(f'No task with {title} in db')
            # Responce
            resp = {
                'status': 404,
                'error msg': f'No task with {title} in db'
            }

        return jsonify(resp)
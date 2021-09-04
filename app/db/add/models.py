from flask import request
from flask import jsonify
from flask_restful import Resource

import datetime

from ..database import init_db
tasks = init_db('user_tasks')

class Add(Resource):
    """
    User Adds new to-do note
    """

    def post(self):
        """
        Gets user post data
        """
        # Get user input
        note = request.get_json()

        user = note['user']  # string
        title = note['title']  # string
        task = note['task']  # string
        task_status = note['status']  # boolean
        
        query = {'Title': title}

        if title is not None and task is not None:
            try:
                db_task_title = tasks.find(query)[0]['Title']
                print(db_task_title)
                if title == db_task_title:
                    task_no = tasks.find(query)[0]['Number'] + 1
                    tasks.update_one(
                        query, 
                        {{ 
                            '$inc': {'Number': 1} ,
                            '$push': {
                                'Tasks': {
                                    f'task_{task_no}': task,
                                    f'task{task_no}_status': task_status
                                }
                            }
                        }}
                    )
                    #  Responce
                    resp = {
                        'status': 202,#accepted
                        'message': f'New task added to {title}.'
                    }
            except IndexError as err:
                print(f'{title} not in DB \nerror: {err}')
                # Store user input in DB
                tasks.insert_one({
                    'Userid': user,
                    'Title': title,
                    'Number': 1,
                    'Created': datetime.datetime.utcnow(),
                    'Tasks': [
                        {
                        'task_1':task,
                        'task1_status':task_status
                        }
                    ]
                })
                # Responce
                resp = {
                    'status': 200, #ok
                    'message': 'Note added'
                }
        else:
            # Responce
            resp = {
                'status': 406, #Not acceptable
                'error msg': 'Not acceptable'
            }

        return jsonify(resp)
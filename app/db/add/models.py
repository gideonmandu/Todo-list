from app import Resource, request, jsonify
from app.db import user_notes

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
        todo = note['todo']  # string
        todo_status = note['status']  # boolean
        
        query = {'Title': title}

        if title is True and todo is True:
            try:
                todo_title = user_notes.find(query)[0]['Title']
                print(todo_title)
                if title == todo_title:
                    task_no = user_notes.find(query)[0]['Number'] + 1;
                    user_notes.update(
                        query, 
                        {{ 
                            '$inc': {'Number': 1} ,
                            '$push': {
                                'Tasks': {
                                    f'todo_task{task_no}': todo,
                                    f'task{task_no}_status': todo_status
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
                user_notes.insert_one({
                    'Userid': user,
                    'Title': title,
                    'Number': 1,
                    'Created': ,
                    'Tasks': [
                        {
                        'todo_task1':todo,
                        'task1_status':todo_status
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
from app import Resource, request, jsonify
from app.db import user_note

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

        # user_note.insert_one({
        #             'Username': user,
        #             'Title': title,
        #             'Tasks': [
        #                 {
        #                 'todo_task1':todo,
        #                 'task1_status':todo_status
        #                 }
        #             ]
        #         })
        # # Responce
        # resp = {
        #     'status': 200,
        #     'message': 'Note added'
        # }
        #todo_title = user_note.find(query)[0]['Title']
		#IndexError: no such item for Cursor instance
        #todo_title = user_note.find({'Title':'lost'})[0]
        #print(todo_title)
        #resp = {
        #    'status': 200,
        #    'message': 'in db'
        #}

        if title is True and todo is True:
            try:
                todo_title = user_note.find(query)[0]['Title']
                print(todo_title)
                if title == todo_title:
                    task_no = user_note.find(query)[0]['Number'] + 1;
                    user_note.update(
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
                        'status': 201,
                        'message': f'New task added to {title}.'
                    }
            except IndexError as err:
                print(f'{title} not in DB \nerror: {err}')
                # Store user input in DB
                user_note.insert_one({
                    'Userid': user,
                    'Title': title,
                    'Number': 1,
                    'Tasks': [
                        {
                        'todo_task1':todo,
                        'task1_status':todo_status
                        }
                    ]
                })
                # Responce
                resp = {
                    'status': 200,
                    'message': 'Note added'
                }
        else:
            # Responce
            resp = {
                'status': 404,
                'error msg': 'No Title and Task in Todo list'
            }

        return jsonify(resp)
from app import Resource, request, jsonify
from app.db import user_note

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
            todo_task = user_note.find({'Title': title})

            # Responce
            resp = {
                'status': 200,
                'task title': f'{todo_task[0]["Title"]}',
                'Task':f'{todo_task[0]["Tasks"][0]["todo_task1"]}'
            }


        except IndexError:
            print(f'No task with {title} in db')
            # Responce
            resp = {
                'status': 404,
                'error msg': f'No task with {title} in db'
            }

        return jsonify(resp)
from app import Resource, request, jsonify
from app.db import user_note

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
        todo = note['todo']  # string

        # search for note in DB then deletes
        try:
            user_note.find_one_and_delete({'Title': title}, {'Tasks':''})

            # Responce
            resp = {
                # ideally use if request.status_code==200
                'status': 200,
                'message': f'Task {todo} in {title} deleted!!!'
            }
        except IndexError:
            print(f'No task with {title} in db')
            # Responce
            resp = {
                'status': 404,
                'error msg': f'No task with {title} in db'
            }
        
        return jsonify(resp)
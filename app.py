"""Start with that one in Flask, then we'll got through it. User should be able to Add new to-do note, delete note, update note. Also user should be able to mark note as complete"""
from flask import Flask, render_template, jsonify, request
from flask_restful import Resource, Api
from pymongo import MongoClient
from pymongo.collection import Collection
from bson.son import SON

app = Flask(__name__)
api = Api(app)

client = MongoClient(host='localhost', port=27017,
                    document_class=dict, tz_aware=False, 
                    connect=True)

db = client.todo_list
user_note = db['todo_notes']


@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    Loads up app page
    """
    return render_template('index.html')


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

        # Store user input in DB
        user_note.insert_one({
            'Username': user,
            'Todolist': [
                SON([
                    ('Title', title),
                    ('Tasks',
                        SON([
                            ('Todo', todo),
                            ('Status', todo_status)
                        ])
                    )
                ])
            ]
        })

        # Responce
        resp = {
            'status': 200,
            'message': 'Note added'
        }
        return jsonify(resp)


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
        todo_task = user_note.find({'Todolist.Title': title})[0]['Todolist']
        #todo_task = user_note.find({'Todolist': SON([('Title', title)])})
        print(todo_task[0]['Title'])

        # Responce
        resp = {
            'status': 200,
            'task title': f'{todo_task[0]["Title"]}',
            'Task':f'{todo_task[0]["Tasks"]["Todo"]}'
        }
        return jsonify(resp)


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
        updated_todo = note['todo']  # string
        updated_task_status = note['status']  # boolean

        # search for note in DB then update
        user_note.create_index({'Title': 1 })
        user_note.create_index({'Todo': 1})
        user_note.update_many(
                {'Todolist.Title': title},
                {'$set': {
                    'Todolist.$[elem].Title': updated_title#,
                    #'Todolist.$[elem].Tasks': {'Todo': updated_todo},
                    #'Todolist.$[elem].Tasks': {'Status': updated_task_status}
                }}, {
                    'upsert': True, 
                    'arrayFilters' :[{'elem.Title': title}]
                }
        )

        # Responce
        resp = {
            'status': 200,
            'task': f'Task Updated'
        }
        return jsonify(resp)


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

        # search for note in DB then deletes
        user_note.find_one_and_delete({'Todolist.Title': title})

        # Responce
        resp = {
            'status': 200,
            'message': f'Task deleted!!!'
        }
        return jsonify(resp)


api.add_resource(Add, '/add')
api.add_resource(Get, '/get')
api.add_resource(Update, '/update')
api.add_resource(Delete, '/delete')

if __name__ == "__main__":
    app.run(debug=True)

from app import config_by_name
# Define the database options which is imported
# by modules and controllers
from pymongo import MongoClient

def db_client(env_state):
    client = MongoClient(
    host= config_by_name[env_state].DB_HOST, 
    port= config_by_name[env_state].DB_PORT,
    document_class= config_by_name[env_state].DOC_CLASS,
    tz_aware=config_by_name[env_state].TZ_AWARE,
    connect=config_by_name[env_state].CON
    )
    return client

def init_db(col_name):
    """
    Build the database: This will create the database and a collection. 
    """
    client = db_client('dev')
    db = client.todolist
    collection = db[col_name]
    return collection
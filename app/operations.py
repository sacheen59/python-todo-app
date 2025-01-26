from database import Database 
from queries import Queries

class TodoApp:
    def __init__(self,db_config):
        self.db = Database(**db_config)

    def initialize_tables(self):
        with self.db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(Queries.CREATE_USERS_TABLE)
                cursor.execute(Queries.CREATE_TODOS_TABLE)
                conn.commit()

    def add_user(self,fullname,email,password):
        with self.db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(Queries.INSERT_USER,(fullname,email,password))
                user_id = cursor.fetchone()['id']
                return user_id
            
    
    def add_todo(self,taskname,description,user_id):
        with self.db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(Queries.INSERT_TODO,(taskname,description,user_id))
                todo_id = cursor.fetchone()['id']
                return todo_id
            
    
    def get_user_by_email(self, email):
        with self.db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(Queries.GET_USER_BY_EMAIL, (email,))
                user = cursor.fetchone()
                return user
            
    def get_todos_by_user(self, user_id):
        with self.db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(Queries.GET_TODOS_BY_USER, (user_id,))
                todos = cursor.fetchall()
                return todos
            
    def update_todo_status(self, todo_id, status):
        with self.db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(Queries.UPDATE_TODO_STATUS, (status, todo_id))
                updated_id = cursor.fetchone()
                return updated_id
            
    def delete_todo(self, todo_id):
        with self.db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(Queries.DELETE_TODO, (todo_id,))
                deleted_id = cursor.fetchone()
                return deleted_id
            
    def drop_tables(self):
        with self.db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(Queries.DROP_ALL_TABLES)
                conn.commit()
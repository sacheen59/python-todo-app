from operations import TodoApp
import os
from dotenv import load_dotenv


load_dotenv()

def main():
    db_config = {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('POSTGRES_USER'),
        'password': os.getenv('POSTGRES_PASSWORD'),
        'host': 'localhost',
        'port': 5432
    }

    app = TodoApp(db_config=db_config)

    app.initialize_tables()

    
    while True:
        print(
            """
                1. Register User
                2. Add Todo
                3. View Todo
                4. Update Todo Status
                5. Delete Todo
                6. Exit
            """
        )

        choice = int(input("Enter the choice: "))

        if choice == 1:
            fullname = input("Fullname: ")
            email = input("Email: ")
            password = input("password: ")
            user_id = app.add_user(fullname,email,password)
            print(f"User added with ID: {user_id}")

        elif choice == 2:
            email = input("User email: ")
            user = app.get_user_by_email(email)
            if user:
                taskname = input("Taskname: ")
                description = input("Description: ")
                todo_id = app.add_todo(taskname,description,user['id'])
                print(f"Todo added with id: {todo_id}")

            else:
                print("user not found")

        elif choice == 3:
            email = input("User Email: ")
            user = app.get_user_by_email(email)
            if user:
                todos = app.get_todos_by_user(user['id'])
                try:
                    with open(f'app/output/{email}.txt','w') as file:
                        for todo in todos:
                            print(f"ID: {todo['id']}, Task: {todo['taskname']}, Status: {'Done' if todo['status'] else 'Pending'}")
                            file.writelines([f"ID: {todo['id']}\n",f"Task: {todo['taskname']}\n",f"Status: {'Done' if todo['status'] else 'Pending'}\n\n"])
                except FileExistsError as e:
                    print(f"error in file: {e}")
            else:
                print("User not found.")
        
        elif choice == 4:
            todo_id = int(input("Todo ID: "))
            status = input("Mark as done? (yes/no): ").strip().lower() == "yes"
            updated = app.update_todo_status(todo_id, status)
            print(f"Todo updated: {updated}")

        elif choice == 5:
            todo_id = int(input("Todo ID: "))
            deleted = app.delete_todo(todo_id)
            print(f"Todo deleted: {deleted}")

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
        


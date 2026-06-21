from tasks import add_task, view_tasks, update_task, delete_task
from app_automation import open_app
from db import close_connection

def run_assistant():
    while True:
        cmd = input("Enter a command (type 'exit' to quit): ").lower().strip()
        if cmd in ["hello", "hi", "hey"]:
            print("Hello! How can I assist you today?")

        elif cmd == "who are you":
            print("I am your personal assistant, here to help you with various tasks.")

        elif cmd == "what can you do":
            print("I can help you with tasks like setting reminders, answering questions, and providing information.") 

        elif "open" in cmd:
            cmd = cmd.split()
            name = " ".join(cmd[1:])
            open_app(name)

        elif cmd == "exit":
            print("Goodbye! Have a great day!")
            close_connection()
            break

        elif "add task" in cmd:
            title = input("Enter the task title: ")
            add_task(title)

        elif "view tasks" in cmd:
            view_tasks()

        elif "update task" in cmd:
            try:
                task_id = int(input("Enter the task ID: "))
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
                continue
            status = input("Enter the new status: ")
            update_task(task_id, status)

        elif "delete task" in cmd:
            try:
                task_id = int(input("Enter the task ID: "))
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
                continue
            delete_task(task_id)

        else:
            print("Sorry, I didn't understand that command. Please try again.")
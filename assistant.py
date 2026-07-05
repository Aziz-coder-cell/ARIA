from tasks import add_task, view_tasks, update_task, delete_task
from app_automation import open_app
from db import close_connection
from ai import ask_gemini, make_plan

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

        elif cmd.startswith("ask"):
            chat_history = []
            prompt = input("What would you like to ask? ")
            while prompt != "back":
                if prompt == '':
                    print("Please enter a valid question.") 
                    prompt = input("What would you like to ask? ") 
                    continue
                chat_history.append({'role':'user','parts' : [{'text': prompt}]})
                response = ask_gemini(chat_history)
                print(f"Gemini's response: {response}")
                prompt = input("Would you like to continue the chat or type 'back' to return to the main menu? ")
        
        elif cmd == "plan my day":
            sub_cmd = 'xyz'
            details = []
            task_details = []
            print("Please enter the tasks you need to complete for the day. Type 'done' when you are finished.")
            date = input("Enter the date for the tasks (YYYY-MM-DD): ")
            while sub_cmd.lower() != "done":
                sub_cmd = input("Enter a task: ")
                if sub_cmd.strip() == "":
                    print("Please enter a valid task name.")
                    continue
                elif sub_cmd.lower() == "done":
                    break
                else:
                    estimated_duration = input("Enter the estimated duration for the task (in hours): ")
                    priority = input("Enter the priority level for the task (low,medium,high): ")
                    details.append(f"Task: {sub_cmd}, estimated_duration: {estimated_duration}, priority: {priority}\n")
            task_details.append({'role': 'user', 'parts': [{'text': f"Date: {date} \n Using the following details, please plan my day and keep the available time in mind:\n"  + ''.join(details)}]})
            text = make_plan(task_details)
            print(f"Gemini's response: {text}")

        else:
            print("Sorry, I didn't understand that command. Please try again.")
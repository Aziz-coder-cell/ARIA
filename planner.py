from ai import make_plan
from tasks import add_task

def details():
    sub_cmd  = 'xyz'
    feedback = "no"
    task_list =[]
    response = ""
    task_details = []
    print("Fill the required details for planning your day. Type 'done' when you are finished.")
    date = input("Enter the date for the tasks (YYYY-MM-DD): ")
    while feedback != 'yes':
        while sub_cmd.lower() != "done":
            sub_cmd = input("Enter a task: ")
            if sub_cmd.strip() == "":
                print("Please enter a valid task name.")
                continue
            elif sub_cmd.lower() == "done":
                break
            elif sub_cmd.lower() == "none":
                print("No additional tasks will be added. Proceeding with the existing tasks.")
                break 
            else:
                estimated_duration = input("Enter the estimated duration for the task (in hours): ")
                priority = input("Enter the priority level for the task (low,medium,high): ")
                task_list.append(f"Task: {sub_cmd}, estimated_duration: {estimated_duration}, priority: {priority}")
        task_details.append({"role": "user","parts": [{'text': f"Date: {date} \n Using the following details,response in short and dont add necessary things I just need a plan and why thats it:\n"  + ''.join(task_list)}]})
        response = make_plan(task_details)
        print(f"Gemini's response: {response}")
        feedback = input("Is this plan acceptable? (yes/no): ")
        while feedback.lower() != 'yes' and feedback.lower() != 'no':
            feedback = input("Please enter a valid response (yes/no): ")
        if feedback.lower() == 'no':
            reason = input("Please provide the reason for not accepting the plan: ")
            task_details.append({"role":"user","parts":[{"text": f"Feedback: {feedback}, Reason: {reason}"}]})
            print("Let's try again. Please provide the details for your tasks if you have missed any or just type none to make an other plan with the same tasks.")
            sub_cmd = 'xyz'
        elif feedback.lower() == 'yes':
            print("Great! Your plan has been accepted.")
    save_choice = input("Do you want to save these tasks? (yes/no): ")
    if save_choice.lower() == 'yes':
        task_name = []
        estimated_duration = []
        priority = []
        for item in task_list:
            task_name.append(item.split(",")[0].split(": ")[1])
            estimated_duration.append(item.split(",")[1].split(": ")[1])
            priority.append(item.split(",")[2].split(": ")[1])
        for i in range(len(task_name)):
            add_task(task_name[i],status='scheduled',scheduled_date=date, estimated_duration=estimated_duration[i], priority=priority[i])
        print("Tasks have been saved successfully.")
    elif save_choice.lower() == 'no':
        print("The tasks will not be saved.")
    else:
        print("Invalid input. The tasks will not be saved.")
    
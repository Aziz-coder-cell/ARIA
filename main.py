import subprocess

def open_app(cmd):
    app_paths = {"brave": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
            "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe"}
    if cmd in app_paths:
        print(f"Opening {cmd}...")
        subprocess.Popen(app_paths[cmd])
    else:
        print(f"Sorry, I couldn't find the application {cmd}...")

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
            break
        else:
            print("Sorry, I didn't understand that command. Please try again.")
            
run_assistant()
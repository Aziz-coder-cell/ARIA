import subprocess

def open_app(cmd):

    app_paths = {
        "brave": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    }

    if cmd in app_paths:
        print(f"Opening {cmd}...")
        subprocess.Popen(app_paths[cmd])

    else:
        print(f"Sorry, I couldn't find the application {cmd}...")
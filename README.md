# ARIA — Action & Response Intelligent Assistant

![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)

ARIA is a lightweight virtual assistant that takes user commands and performs actions like opening applications and responding to basic queries.

---

## What It Does
- Accepts text-based user commands
- Responds to greetings and basic questions 
- Opens applications using system commands

---

## Features (Current)
> This is the first feature of the ARIA project.

- Text-based assistant (command input system)
- Basic conversation (hello, who are you, etc.)
- App automation (open apps like Chrome, Brave)

---

## Supported Commands
| Command | Response |
|---|---|
| hello / hi / hey | Greeting response |
| who are you | Assistant introduction |
| what can you do | Lists capabilities |
| open chrome / open brave | Opens the application |
| exit | Exits the assistant |

> **Note:** Commands are case-insensitive but punctuation-sensitive. Type commands exactly as shown above.

---

## Demo

**Assistant Running:**
![Project Setup](assets/Screenshot(1).png)

---

## Tech Stack
- Python
- subprocess (built-in Python module)

---

## How to Run

1. Clone the repository:
```bash
git clone <your-repo-link>
cd <repo-folder>
```

2. Run the assistant:
```bash
python aria.py
```

> **Note:** App paths in `open_app()` are set for Windows. Update the paths in the `app_paths` dictionary inside `aria.py` to match your system.

---

## Note
This is an early-stage project, actively being developed. More features like AI Q&A, task management, and voice integration will be added progressively.

---

## Connect
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/mohammed-abdul-aziz-/)
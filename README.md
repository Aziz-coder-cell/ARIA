# ARIA — Action & Response Intelligent Assistant

![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)

ARIA is a lightweight virtual assistant that executes user commands, automates desktop tasks, manages tasks using MySQL, and answers user queries using Google's Gemini AI.

---

## What It Does

- Accepts text-based user commands
- Automates desktop applications
- Manages tasks using MySQL (CRUD operations)
- Answers questions using Google Gemini AI

---

## Features (Current — Feature 1 to Feature 4 Completed)

### Feature 1 — Text-Based Assistant

- Accepts text-based user commands
- Basic conversation
- Command handling

### Feature 2 — App Automation

- Opens desktop applications
- Supports Chrome and Brave
- Executes system-level commands

### Feature 3 — Task Management

- Add tasks
- View tasks
- Update task status
- Delete tasks
- Persistent storage using MySQL

### Feature 4 — AI Q&A

- Ask questions using Google Gemini
- Multi-turn conversation
- Secure API key management using environment variables
- Error handling for API failures

---

## Supported Commands

| Command | Action |
|---------|--------|
| hello / hi / hey | Greeting response |
| who are you | Assistant introduction |
| what can you do | Lists capabilities |
| open chrome | Opens Chrome |
| open brave | Opens Brave |
| add task | Adds a task |
| view tasks | Displays all tasks |
| update task | Updates task status |
| delete task | Deletes a task |
| ask | Starts an AI conversation |
| exit | Closes the assistant |

> Commands are case-insensitive and punctuation-sensitive.

---

## Architecture Flow

```text
                 User
                   │
                   ▼
             Assistant
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
 App Automation   MySQL     Gemini API
      │            │            │
      ▼            ▼            ▼
 Opens Apps     CRUD Tasks   AI Responses
```

---

## Demo

### Feature 1 — Text-Based Assistant & App Automation

![Assistant Demo](assets/Screenshot(1).png)

---

### Feature 3 — Task Management (CRUD)

Supports:
- Add task
- View tasks
- Update task status
- Delete task

![Task Management Demo](assets/Screenshot%20(2)CRUD.png)

---

### Feature 4 — AI Q&A

Supports:
- Ask questions using Gemini AI
- Continue conversation
- Return to the main menu

![AI Q&A Demo](assets/Screenshot%20(3).png)

---

## Tech Stack

- Python
- MySQL
- PyMySQL
- Google Gemini API
- python-dotenv
- subprocess

---

## Requirements

- Python 3.10+
- MySQL Server
- Google Gemini API Key

---

## Project Structure

```text
ARIA/
├── assets/
│   ├── Screenshot(1).png
│   ├── Screenshot (2)CRUD.png
│   └── Screenshot (3).png
├── ai.py
├── app_automation.py
├── assistant.py
├── db.py
├── main.py
├── tasks.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Aziz-coder-cell/ARIA.git
cd ARIA
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure MySQL

Create the database:

```sql
CREATE DATABASE aria_db;
```

Create the table:

```sql
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(225),
    status VARCHAR(50)
);
```

### 4. Configure Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

Open `.env` and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

> **Windows users:** If `cp` is unavailable, simply duplicate `.env.example` and rename the copy to `.env`.

### 5. Run the project

```bash
python main.py
```

---

## Upcoming Features

- Planning Assistant
- PPT Generation
- Research Assistant
- Voice Integration
- Smart System Automation
- File Management
- Calendar & Reminder Integration
- Email Automation
- Web Search & Summarization
- Personal Knowledge Base

---

## Connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/mohammed-abdul-aziz-/)

---

⭐ ARIA is an actively developed project. New features and improvements will be added progressively.
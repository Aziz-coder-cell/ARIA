# ARIA — Action & Response Intelligent Assistant

![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)

ARIA is a lightweight AI-powered personal assistant built in Python that executes user commands, automates desktop tasks, manages tasks using MySQL, answers questions using Google's Gemini AI, and helps users plan their day intelligently.

---

## What It Does

- Accepts text-based user commands
- Automates desktop applications
- Manages tasks using MySQL (CRUD operations)
- Answers questions using Google Gemini AI
- Generates AI-powered daily schedules based on tasks and priorities

---

## Features

### ✅ Feature 1 — Text-Based Assistant

- Accepts text-based commands
- Basic conversation
- Command routing

---

### ✅ Feature 2 — App Automation

- Opens desktop applications
- Supports launching Chrome and Brave
- Executes system-level commands

---

### ✅ Feature 3 — Task Management

- Add tasks
- View tasks
- Update task status
- Delete tasks
- Persistent storage using MySQL

---

### ✅ Feature 4 — AI Q&A

- Ask questions using Google Gemini
- Multi-turn conversations
- Secure API key management using environment variables
- Error handling for API failures

---

### 🟡 Feature 5 — Smart Day Planner (In Progress)

Generate a structured day plan by providing:

- Date
- Tasks
- Estimated duration
- Priority level

ARIA generates a personalized daily schedule using Google Gemini AI.

- Focus blocks
- Breaks
- Meal timings
- Buffer time
- Productivity suggestions

> **Status:** Working but still under development with more improvements planned.

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
| plan my day | Generates an AI-powered daily schedule |
| exit | Closes the assistant |

> Commands are case-insensitive.

---

## Architecture Flow

```text
                    User
                      │
                      ▼
                Assistant
      ┌──────────┼──────────┬──────────┐
      ▼          ▼          ▼          ▼
 App Automation MySQL    Gemini AI   Day Planner
      │          │          │          │
      ▼          ▼          ▼          ▼
 Opens Apps   CRUD Tasks AI Answers Daily Schedule
```

---

## Demo

### Feature 1 — Text Assistant & App Automation

![Assistant Demo](assets/Screenshot(1).png)

---

### Feature 3 — Task Management

Supports:

- Add Task
- View Tasks
- Update Task
- Delete Task

![Task Management](assets/Screenshot%20(2)CRUD.png)

---

### Feature 4 — AI Q&A

Supports:

- Ask questions
- Multi-turn conversation
- Return to main menu

![AI Demo](assets/Screenshot%20(3).png)

---

### Feature 5 — Smart Day Planner

Provide:

- Date
- Tasks
- Estimated duration
- Priority

ARIA generates an optimized schedule using Gemini AI.

### Input

![Planner Input](assets/Screenshot%20(4).png)

### Generated Plan

![Planner Output 1](assets/Screenshot%20(5).png)

![Planner Output 2](assets/Screenshot%20(6).png)

---

## Tech Stack

- Python
- MySQL
- PyMySQL
- Google Gemini 2.5 Flash Lite
- Google GenAI SDK
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
│
├── assets/
│   ├── Screenshot(1).png
│   ├── Screenshot (2)CRUD.png
│   ├── Screenshot (3).png
│   ├── Screenshot (4).png
│   ├── Screenshot (5).png
│   └── Screenshot (6).png
│
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

Create the `tasks` table:

```sql
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(225),
    status VARCHAR(50),
    scheduled_date DATE,
    estimated_duration TIME,
    priority VARCHAR(30)
);
```

| Column | Description |
|---------|-------------|
| id | Unique task ID |
| title | Task title |
| status | Current task status (e.g., pending, completed) |
| scheduled_date | Date assigned to the task |
| estimated_duration | Estimated time required to complete the task |
| priority | Priority level (Low, Medium, High) |

### 4. Configure Environment Variables

Copy

```bash
cp .env.example .env
```

Add your API key

```env
GEMINI_API_KEY=your_api_key_here
```

> Windows users can simply duplicate `.env.example` and rename it to `.env`.

### 5. Run the project

```bash
python main.py
```

---

## Roadmap

### ✅ Completed

- Text-Based Assistant
- App Automation
- Task Management (MySQL CRUD)
- AI Q&A

### 🟡 In Progress

- Smart Day Planner

### ⏳ Planned

- PPT Generation
- Research Assistant
- Voice Integration
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
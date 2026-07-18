# ARIA — Action & Response Intelligent Assistant

![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)

ARIA is a lightweight AI-powered personal assistant built in Python that executes user commands, automates desktop tasks, manages tasks using MySQL, answers questions using Google's Gemini AI, and intelligently plans your day.

---

## What It Does

- Accepts text-based user commands
- Automates desktop applications
- Manages tasks using MySQL (CRUD operations)
- Answers questions using Google Gemini AI
- Generates AI-powered daily schedules
- Saves accepted plans for future reference
- Generates AI-powered PowerPoint presentations

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

### ✅ Feature 5 — Smart Day Planner

Generate an AI-powered daily schedule by providing:

- Date
- Tasks
- Estimated duration
- Priority level

Features:

- AI-generated schedule
- User feedback loop (accept/reject)
- Regenerates plan based on feedback
- Save accepted plans to MySQL
- View saved plans anytime

---

### ✅ Feature 6 — AI PPT Generation

Generate a PowerPoint presentation by providing:

- Presentation topic
- Number of slides

Features:

- AI-generated slide titles and bullet points
- Automatic `.pptx` generation using `python-pptx`
- Saves the presentation locally

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
| view plan | Displays saved daily plans |
| make presentation | Generates an AI-powered PowerPoint presentation |
| exit | Closes the assistant |

> Commands are case-insensitive.

---

## Architecture Flow

```text
                              User
                                │
                                ▼
                      Assistant (Command Router)
                                │
      ┌──────────┬──────────┬──────────┬────────────────┐
      ▼          ▼          ▼          ▼                ▼
App Automation   Tasks      AI Q&A    Planner     PPT Generator
      │           │            │          │             │
      ▼           ▼            ▼          ▼             ▼
 Opens Apps   MySQL CRUD   Gemini API  Gemini API  Gemini API
                  ▲                        │            │
                  │                        ▼            ▼
                  │               Generate Plan   Generate Slides
                  │                        │            │
                  └──────────────┬─────────┘            │
                                 ▼                      ▼
                       Save Scheduled Tasks      Create .pptx File
                                 │
                                 ▼
                          View Saved Plan
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

#### Generated Plan

![Planner Output](assets/Screenshot%20(4).png)

#### View Saved Plan

![View Plan](assets/Screenshot%20(5).png)

---

### Feature 6 — AI PPT Generation

Provide:

- Presentation topic
- Number of slides

ARIA generates slide content using Gemini AI and automatically creates a PowerPoint presentation.

#### PPT Generation

![PPT Generation](assets/Screenshot%20(6).png)

---

## Tech Stack

- Python
- MySQL
- PyMySQL
- Google Gemini API (2.5 Flash Lite)
- Google GenAI SDK
- Google AI Studio
- python-dotenv
- subprocess
- python-pptx

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
├── planner.py
├── tasks.py
├── db.py
├── ppt.py
├── main.py
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
    estimated_duration DECIMAL(4,2),
    priority VARCHAR(30)
);
```

| Column | Description |
|---------|-------------|
| id | Unique task ID |
| title | Task title |
| status | Current task status |
| scheduled_date | Scheduled task date |
| estimated_duration | Estimated completion time |
| priority | Task priority |

### 4. Configure Environment Variables

Copy:

```bash
cp .env.example .env
```

Add your API key:

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
- Smart Day Planner
- PPT Generation

### ⏳ Planned

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

⭐ ARIA is actively being developed. Each feature builds toward a fully autonomous AI-powered personal assistant.
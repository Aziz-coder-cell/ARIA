# ARIA — Action & Response Intelligent Assistant

![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)

ARIA is a lightweight virtual assistant that executes user commands, automates actions, and manages tasks using a modular Python architecture.

---

## What It Does

* Accepts text-based user commands
* Responds to greetings and assistant queries
* Opens desktop applications
* Manages tasks using MySQL (CRUD operations)

---

## Features (Current — Feature 1 & Feature 2 Completed)

### Feature 1 — Assistant + Automation

* Text-based assistant
* Basic conversation
* App automation

### Feature 2 — Task Management

* Add tasks
* View tasks
* Update task status
* Delete tasks
* Persistent storage using MySQL

---

## Supported Commands

| Command          | Action                 |
| ---------------- | ---------------------- |
| hello / hi / hey | Greeting response      |
| who are you      | Assistant introduction |
| what can you do  | Lists capabilities     |
| open chrome      | Opens Chrome           |
| open brave       | Opens Brave            |
| add task         | Adds task              |
| view tasks       | Displays tasks         |
| update task      | Updates task status    |
| delete task      | Deletes task           |
| exit             | Closes assistant       |

> Commands are case-insensitive and punctuation-sensitive.

---

## Architecture Flow

```plaintext
User → Assistant → Command Handler → App / Database
```

---

## Demo

### Feature 1 — Assistant + Automation

![Assistant Running](assets/Screenshot\(1\).png)

### Feature 2 — Task Management (CRUD)

Supports:

* Add task
* View tasks
* Update task status
* Delete task

![Task Management Demo](assets/Screenshot%20(2)CRUD.png)

---

## Tech Stack

* Python
* MySQL
* PyMySQL
* subprocess

---

## Requirements

* Python 3.x
* MySQL installed

---

## Project Structure

```plaintext
ARIA/
├── main.py
├── assistant.py
├── app_automation.py
├── tasks.py
├── db.py
├── assets/
│ ├── Screenshot(1).png
│ └── Screenshot(2).png
├── requirements.txt
└── README.md
```

---

## How to Run

### 1. Clone repository

```bash
git clone https://github.com/Aziz-coder-cell/ARIA.git
cd ARIA
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure database

Create database:

```sql
CREATE DATABASE aria_db;
```

Create table:

```sql
CREATE TABLE tasks(
id INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(225),
status VARCHAR(50)
);
```

### 4. Run project

```bash
python main.py
```

---

## Upcoming Features

* AI Q&A
* Planning assistant
* PPT generation
* Research support
* Voice integration

---

## Connect
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/mohammed-abdul-aziz-/)
from db import connection, cursor
import pymysql

def add_task(title, status='pending'):
    mysql = "insert into tasks(title,status) values (%s,%s)"
    try:
        cursor.execute(mysql, (title, status))
        connection.commit()
    except pymysql.MySQLError:
        print("Error: Unable to add task.")
        connection.rollback()

def view_tasks():
    mysql = "select * from tasks"
    try:
        cursor.execute(mysql)
        tasks = cursor.fetchall()
    except pymysql.MySQLError:
        print("Error: Unable to retrieve tasks.")
        return
    for task in tasks:
        print(f"ID: {task[0]}, Title: {task[1]}, Status: {task[2]}")

def update_task(task_id, status):
    mysql = "update tasks set status=%s where id=%s"
    mysql_2 = "select * from tasks where id=%s"
    try:
        result = cursor.execute(mysql, (status, task_id))
        result_2 = cursor.execute(mysql_2, (task_id,))
    except pymysql.MySQLError:
        print("Error: Unable to update task.")
        connection.rollback()
        return
    if result == 0 and result_2 == 0:
        print("Task not found.")
        return
    try:
        connection.commit()
        print(f"Task with ID {task_id} updated successfully.")
    except pymysql.MySQLError:
        print("Error: Unable to commit changes.")
        connection.rollback()

def delete_task(task_id):
    mysql = "delete from tasks where id=%s"
    try:
        result = cursor.execute(mysql, (task_id,))
    except pymysql.MySQLError:
        print("Error: Unable to delete task.")
        connection.rollback()
        return
    if result == 0:
        print("Task not found.")
    else:
        try:
            connection.commit()
            print(f"Task with ID {task_id} deleted successfully.")
        except pymysql.MySQLError:
            print("Error: Unable to commit changes.")
            connection.rollback()
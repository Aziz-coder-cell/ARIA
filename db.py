import pymysql

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database= "aria_db"
)

cursor = connection.cursor()

def close_connection():
    cursor.close()
    connection.close()
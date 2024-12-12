import mysql.connector

myDB =mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Uikey@06'
)

my_cursor =myDB.cursor()

my_cursor.execute('CREATE DATABASE users')

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)
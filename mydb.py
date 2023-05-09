import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

# Create a cursor object

cursorObj = dataBase.cursor()

cursorObj.execute("CREATE DATABASE crm")

print("DB created successfully !!")
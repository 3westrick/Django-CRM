import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="Amir1380"
)

cursor = db.cursor()
# cursor.execute("CREATE DATABASE mydb")
print("All done...")

# Q28. Update and delete records

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="testdb"
)

cur = con.cursor()

cur.execute("update student set name='Gannu' where id=1")
cur.execute("delete from student where id=1")

con.commit()
print("Updated and Deleted")
# Q26. MySQL create table and insert

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="testdb"
)

cur = con.cursor()

cur.execute("create table if not exists student(id int, name varchar(20))")
cur.execute("insert into student values(1,'Simmi')")

con.commit()
print("Inserted Successfully")
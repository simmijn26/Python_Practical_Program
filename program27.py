# Q27. Retrieve and display records

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="testdb"
)

cur = con.cursor()

cur.execute("select * from student")

for row in cur.fetchall():
    print(row)
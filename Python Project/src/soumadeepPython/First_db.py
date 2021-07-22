import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="upload"
)

cur = con.cursor()
cur.execute("SELECT * FROM imgupload")
tb = cur.fetchall()
for i in tb:
    print(tb)

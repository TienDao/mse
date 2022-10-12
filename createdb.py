import sqlite3 as sql

#connect to SQLite
con = sql.connect('students.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS users")

#Create users table  in db_web database
sql ='''CREATE TABLE "students" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT,
	"email" TEXT, 
	"birthday" TEXT,
	"address"	TEXT,
	"score" TEXT
)'''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()
import sqlite3 as sql

con = sql.connect('students.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS users")
sql ='''CREATE TABLE "students" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT,
	"email" TEXT, 
	"birthday" TEXT,
	"address"	TEXT,
	"score" TEXT
)'''
cur.execute(sql)
con.commit()
con.close()
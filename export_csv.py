import sqlite3 as sql
import csv

f = open('csv.csv', 'w', newline='', encoding="utf-8")
writer = csv.writer(f)
con = sql.connect("students.db")
cur = con.cursor()
cur.execute("select * from students")
datas = cur.fetchall()
for data in datas:
    writer.writerow(data)
f.close()


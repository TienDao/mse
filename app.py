from flask import Flask, render_template, request, redirect, url_for, Response
import sqlite3 as sql


app = Flask(__name__)


@app.route("/export_xml")
def export_xml():
    xml = ''
    con = sql.connect("students.db")
    cur = con.cursor()
    cur.execute("select * from students")
    datas = cur.fetchall()
    xml += "<students>"
    for data in datas:
        xml += "<student>"
        xml += "<id>"+ str(data[0])+"</id>"
        xml += "<name>" + str(data[1]) + "</name>"
        xml += "<email>" + str(data[2]) + "</email>"
        xml += "<birthday>" + str(data[3]) + "</birthday>"
        xml += "<address>" + str(data[4]) + "</address>"
        xml += "<score>" + str(data[5]) + "</score>"
        xml += "</student>"
    xml += "</students>"
    return Response(xml, mimetype='text/xml; charset=utf-8')


@app.route("/")
@app.route("/index")
def index():
    con = sql.connect("students.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from students")
    data = cur.fetchall()
    return render_template("index.html", datas=data)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        birthday = request.form['birthday']
        address = request.form['address']
        score = request.form['score']
        con = sql.connect("students.db")
        cur = con.cursor()
        cur.execute("insert into students(name, email, birthday, address, score) values (?,?,?,?,?)", (name, email, birthday, address, score))
        con.commit()
        return redirect(url_for("index"))
    return render_template("add.html")


@app.route("/edit/<string:id>", methods=['POST', 'GET'])
def edit(id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        birthday = request.form['birthday']
        address = request.form['address']
        score = request.form['score']
        con = sql.connect("students.db")
        cur = con.cursor()
        cur.execute("update students set name=?, email=?, birthday=?,address=?,score=? where id=?", (name, email, birthday, address, score, id))
        con.commit()
        return redirect(url_for("index"))
    con = sql.connect("students.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from students where id=?", (id,))
    data = cur.fetchone()
    return render_template("edit.html", datas=data)


@app.route("/delete/<string:id>", methods=['GET'])
def delete(id):
    con = sql.connect("students.db")
    cur = con.cursor()
    cur.execute("delete from students where id=?", (id,))
    con.commit()
    return redirect(url_for("index"))

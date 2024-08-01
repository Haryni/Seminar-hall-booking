from flask import Flask,render_template,redirect,request
import sqlite3

app=Flask(__name__)
con=sqlite3.connect("database.db")
cur=con.cursor()
cur.execute("create table if not exists login(pid integer primary key,name text,password text)")
con.close()
@app.route('/')
def index():
    image_path=["/static/images/1.avif",
                 "/static/images/2.jpg",
                 "/static/images/3.jpg",
                 "/static/images/4.jpeg",
                 "/static/images/5.avif",
                 "/static/images/9.jpg",
                 "/static/images/5.jpg",
                 "/static/images/7.jpg",
                 "/static/images/8.jpg",
                 "/static/images/main.webp"
    ]   
         

    return render_template("index.html",image_path=image_path)
@app.route('/book')
def book():
    return render_template("book.html")
@app.route('/select')
def select():
    return render_template("select.html")
if __name__=="__main__":
    app.run(debug=True)
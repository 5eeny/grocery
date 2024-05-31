import os
from flask import Flask, flash
from flask import render_template, request, url_for, redirect, session
from flask_session import Session
from flask import request

from flask_sqlalchemy import SQLAlchemy

current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, "grocerydb.sqlite3")

db=SQLAlchemy()
db.init_app(app)
app.app_context().push()

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    uname = db.Column(db.String, unique=True)
    pwd = db.Column(db.String)

class Category(db.Model):
    __tablename__ = 'category'
    cid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cname = db.Column(db.String, unique=True)

class Product(db.Model):
    __tablename__ = 'product'
    pid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    pname = db.Column(db.String, unique=True)
    pcategory = db.Column(db.String)
    unit = db.Column(db.String, unique=True)
    r8punit = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

class Cart(db.Model):
    __tablename__ = 'cart'
    cartid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cartquant = db.Column(db.Integer, unique=True)
    cartprice = db.Column(db.Integer)
    subtotal = db.Column(db.Integer)


@app.route('/', methods=["GET","POST"])
def home():
    return render_template("userornot.html")


@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("uname")
        password = request.form.get("pword")
        user1 = User.query.filter_by(uname=username).first()
        if user1 and user1.check_password(password):
            return render_template("products.html", name=request.form.get("uname")) 
        else:
            return ("loginreg.html")

@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("registration.html")
    else:
        username = request.form.get("uname")
        password = request.form.get("pword")
        db.create_all()
        new_user = User(uname=username, pwd=password)
        db.session.add(new_user)
        db.session.commit()
        return render_template("loginreg.html")


@app.route('/prods', methods=["GET","POST"])
def products():
    return render_template("products.html", name=request.form.get("uname"))


    
@app.route('/logout')
def logout():
    return render_template('/')



if __name__== '__main__':
    app.run(
        host = '0.0.0.0',
        debug=True,
        port=8080
    )





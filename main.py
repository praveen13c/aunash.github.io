# Aum Shree Ganeshaay Namah

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
from datetime import datetime


with open("config.json", "r") as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-tvnytc@gmail.com'],
    MAIL_PASSWORD=params['gmail-TVN@yt0517']
)
mail = Mail(app)

if(local_server):
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:NEGU@phpma4psc@localhost/aunash'
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]

db = SQLAlchemy(app)

class Contact(db.Model):

    srno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    # name = db.Column(db.String(80), unique=False, nullable=False)
    phone_num = db.Column(db.String(12),  nullable=False)
    email = db.Column(db.String(20),  nullable=False)
    date = db.Column(db.String(12), nullable=True)
    msg = db.Column(db.String(120),  nullable=False)

@app.route("/")
def home():
    return render_template("index.html" , params=params)

@app.route("/about")
def about():
    return render_template("about.html" , params=params)

@app.route("/post")
def post():
    return render_template("post.html" , params=params)

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        """ add entry to the database"""
        name= request.form.get('name')
        email= request.form.get('email')
        phone= request.form.get('phone')
        message= request.form.get('message')

        entry = Contact(db_name=name, db_phone_num=phone, db_message=message, db_date=datetime.now(),
                        db_email=email)
        db.session.add(entry)
        db.session.commit()

    return render_template("contact.html" , params=params)

@app.route("/media")
def media():
    return render_template("media.html" , params=params)

app.run(debug=True)
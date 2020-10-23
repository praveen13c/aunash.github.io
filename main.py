# www.aunash.com website backend coding
# Coder = Praveen Singh Chauhan        GitHub = https://github.com/praveen13c
# Credit = Mohd.Haris Ali Khan from Code with Harry
# Credit = https://stackoverflow.com/  https://flask.palletsprojects.com/

# Program Starts

# import section
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime
import pymysql
import json

# opening config.json file in read mode in a variable and  assign to params to read all params from config.json
with open('config.json', 'r') as a:
    params_1 = json.load(a)["params"]
# lo_params = layout.html variable     params_1 = main.py variable   params = config.json variable

local_server = True
pymysql.install_as_MySQLdb()  # getting errors so ive to make this line Credit - stackoverflow.com
app = Flask(__name__)

# app will give access to personal email
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT ='465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params_1['gmail_user'],
    MAIL_PASSWORD = params_1['gmail_password']
)
mail = Mail(app)   # mall variable assign to Mail(app)

# Condition handle
if(local_server):
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/aunash'    <-- this is original line
    # if local server is True then its a local server
    app.config['SQLALCHEMY_DATABASE_URI'] = params_1['local_uri']
else:
    # if local server is False then its a production server
    app.config['SQLALCHEMY_DATABASE_URI'] = params_1['prod_uri']

db = SQLAlchemy(app)   # db variable assign from SQLAlchemy(app)

# making a class of Contact with database model where column, data type and length determine from here
class Contact(db.Model):
    # all variables of database are handle here
    cont_srno = db.Column(db.Integer, primary_key=True)
    cont_name = db.Column(db.String(80), nullable=False)
    cont_email = db.Column(db.String(20), nullable=False)
    cont_phone_num = db.Column(db.String(12), nullable=False)
    cont_message = db.Column(db.String(150), nullable=False)
    cont_date = db.Column(db.String(12), nullable=True)


@app.route("/")
def home():

    return render_template("index.html", lo_params=params_1)


@app.route("/services")
def services():

    return render_template("services.html", lo_params=params_1)


@app.route("/blog_post")
def post():

    return render_template("blog_post.html", lo_params=params_1)


@app.route("/vlog")
def about():

    return render_template("vlog.html", lo_params=params_1)

# we give methods GET means it always use this method to get anything and by POST we will post our inputs in database
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    # condition handle
    if(request.method == 'POST'):
        # variable request from form or html to get variable inputs , main.py variable = contact.html input
        # assigning main.py variable inputs coming from contact.html
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        # we give entry form Contact class and tell name(from database) = name(from request html get)
        # database variable = main.py variable
        # main.py variable processing with Contact class and assigned values giving to database variables
        entry = Contact(cont_name=name, cont_email=email, cont_phone_num=phone, cont_message=message,
                        cont_date=datetime.now())
        db.session.add(entry) # our entry will be add to store in database
        db.session.commit() # we commit or confirm our entry to save in database
        # this will send message to personal email also
        mail.send_message('New Message of ' + name + ' from Aunash ',  # name of sender
                          sender =  email, # alongwith email of sender
                          recipients = [params_1['gmail_user']], # authorization to personal email
                          body = message + '\n' + phone # alongwith message and phone number of sender
                          )
    # returning process by render the templates of html and assigning main.py value to layout.html variable
    # layout.html variable = main.py variable
    return render_template("contact.html", lo_params=params_1)

# trigger app to run and if any changes occur it will recognize and re-run the program automatically
app.run(debug=True)

# End Program
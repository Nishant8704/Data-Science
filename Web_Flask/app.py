from flask import Flask,render_template, request

from db import Database

app = Flask(__name__)

dbo  = Database()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods = ['post'])
def perform_registration():
    name = request.form.get('user_ka_name')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.insert(name,email,password)
    if response:
        return "Registration Successfull"
    else:
        return "Email Already Exist!"

app.run(debug = True)
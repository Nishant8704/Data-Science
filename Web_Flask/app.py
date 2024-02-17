from flask import Flask, redirect,render_template, request,session
from db import Database
import api

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
        return render_template('login.html',message = "Registration Successfull. Kindly Login to Proceed")
    else:
        return render_template('register.html',message = "Email Already Exists!!")
    
@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get('user_ka_email')
    password =  request.form.get('user_ka_password')

    response = dbo.search(email,password)
    if response:
        session['logged_in']=1
        return redirect('/profile')      #import redirect 
    else:
        return render_template("login.html",message="Sorry, You have entered wrong Information.")
    
@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')


@app.route('/ner')
def ner():
    if session:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner',methods = ['post'])
def perform_ner():
    if session:
        text = request.form.get('ner_text')
        response = api.ner(text)
        print(response)
        return render_template("ner.html",response=response)
    else:
        return redirect('/')

app.run(debug = True)
from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)


# from flask_app.models.user_model import User


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sign_up', methods = ['POST'])
def sign_up():
    if not User.validate_sign_up(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['pass'])
    # print(pw_hash)
    data = {
        'first_name':request.form['fname'],
        'last_name':request.form['lname'],
        'email':request.form['email'],
        'password':pw_hash
    }
    user_id = User.save(data)
    
    session['user_id'] = user_id

    return redirect('/dashboard')


@app.route('/login', methods = ['POST'])
def login():
    data = { "email" : request.form["lemail"] }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['lpass']):
        flash("Invalid Email/Password")
        return redirect('/')
    
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    return render_template('dashboard.html', user = User.get_one(session['user_id']))


@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')
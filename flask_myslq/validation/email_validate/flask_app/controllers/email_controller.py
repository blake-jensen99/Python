from flask import Flask, render_template, redirect, request, session

from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import app

from flask_app.models.email_model import Email



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/success')
def sucess():
    return render_template("success.html", all_emails = Email.get_all())


@app.route('/add_email', methods = ['POST'])
def add_email():
    data = {'email':request.form['email']}
    print (data)
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.save(data)
    return redirect('/success')
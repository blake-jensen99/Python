from flask import Flask, render_template, redirect, request

from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import app

from flask_app.models.ninja_model import Ninja

from flask_app.models.dojo_model import Dojo

@app.route('/new_ninja')
def new_ninja():
    
    return render_template('new_ninja.html', dojos = Dojo.get_all())


@app.route('/create_ninja', methods = ['POST'])
def create_ninja():

    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"],
        "dojo_id":request.form["dojo_id"]
    }
    Ninja.save(data)
    id = data["dojo_id"]
    return redirect(f'/show/{id}')


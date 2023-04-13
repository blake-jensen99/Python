from flask import Flask, render_template, redirect, request

from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import app

from flask_app.models.dojo_model import Dojo


@app.route("/dojos")
def index():
    # call the get all classmethod to get all users
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("index.html", all_dojos = dojos)


@app.route('/create_dojo', methods=["POST"])
def create_dojo():

    data = {
        "name": request.form["name"],
    }
    
    Dojo.save(data)

    return redirect('/dojos')

@app.route("/show/<int:id>")
def show_dojo(id):

    return render_template("show_dojo.html", dojo=Dojo.get_dojos_with_ninjas(id))
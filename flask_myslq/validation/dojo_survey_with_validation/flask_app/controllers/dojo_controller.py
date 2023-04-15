from flask import Flask, render_template, redirect, request, session

from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import app

from flask_app.models.dojo_model import Dojo



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():


    data = {
        'name' : request.form['name'],
        'location' : request.form['location'],
        'language' : request.form['language'],
        'comment' : request.form['comment']
    }
    print(data)

    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    
    id  = Dojo.save(data)
    

    return redirect(f'/result/{id}')


@app.route('/result/<int:id>')
def result(id):
    return render_template("result.html", dojo = Dojo.get_one(id))


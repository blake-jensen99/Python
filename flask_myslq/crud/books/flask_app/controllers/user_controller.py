from flask import Flask, render_template, redirect, request

from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import app
from flask_app import DB

from flask_app.models.user_model import User
from flask_app.models.book_model import Book







@app.route("/")
def index_users():
    users = User.get_all()
    return render_template("users.html", all_users = users)



@app.route('/create_user', methods=["POST"])
def create_user():
    

    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
    }
    
    User.save(data)

    return redirect('/')


@app.route("/users/<int:id>")
def show_users(id):
    
    

    return render_template("show_user.html", user=User.get_users_with_books(id), book = Book.get_all())


@app.route('/add_book', methods = ['POST'])
def add_book():

    data = {
        "user_id":request.form["user_id"],
        "book_id":request.form["book_id"]
        
    }

    User.add_book(data)
    id = data["user_id"]
    return redirect(f'/users/{id}')

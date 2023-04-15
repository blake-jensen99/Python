from flask import Flask, render_template, redirect, request

from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import app
from flask_app import DB

from flask_app.models.book_model import Book
from flask_app.models.user_model import User




@app.route("/books")
def index_books():
    books = Book.get_all()
    return render_template("books.html", all_books = books)




@app.route('/create_book', methods=["POST"])
def create_book():

    data = {
        "title": request.form["title"],
        'pages':request.form['pages']
    }
    
    Book.save(data)

    return redirect('/books')


@app.route("/books/<int:id>")
def show_book(id):
    return render_template("show_book.html", book=Book.get_books_with_users(id), user = User.get_all())


@app.route('/add_user', methods = ['POST'])
def add_user():

    data = {
        "user_id":request.form["user_id"],
        "book_id":request.form["book_id"]
        
    }

    Book.add_user(data)
    id = data["book_id"]
    return redirect(f'/books/{id}')
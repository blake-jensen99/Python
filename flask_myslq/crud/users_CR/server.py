from flask import Flask, render_template, redirect, request
# import the class from user.py
from user import User

from mysqlconnection import connectToMySQL
app = Flask(__name__)


@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)
            


@app.route("/add_user")
def user_form():

    return render_template("new.html")


@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
    }
    
    
    # We pass the data dictionary into the save method from the User class.
    User.save(data)

    query = "SELECT id FROM users ORDER BY id DESC LIMIT 1;"
    result = connectToMySQL('users').query_db(query)
    id = result[0]['id']
    print(id)
    # Don't forget to redirect after saving to the database.
    return redirect(f'/show/{id}')


@app.route("/show/<int:id>")
def show_user(id):

    return render_template("show.html", user=User.get_one(id))



@app.route('/edit/<int:id>')
def updateform(id):
    
    return render_template('edit.html', user=User.get_one(id))


@app.route('/save_update', methods=['POST'])
def updatesave():
    print(request.form)
    User.update(request.form)

    id = request.form['id']
    print(id)
    # Don't forget to redirect after saving to the database.
    return redirect(f'/show/{id}')




@app.route('/delete/<int:id>')
def delete(id):
    # print(id)
    User.delete(id)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

 
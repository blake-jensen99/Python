from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['loca'] = request.form['loca']
    session['leng'] = request.form['leng']
    session['comment'] = request.form['comment']
    return redirect('/result')


@app.route('/result')
def result():
    return render_template("result.html")

@app.route('/clear')
def clear():
    session.clear()
    return redirect("/")





if __name__=="__main__":
    app.run(debug=True)
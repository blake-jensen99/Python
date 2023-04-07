from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if not 'x' in session:
        session['x'] = 0
        
    session['x'] += 1
    return render_template("index.html")

@app.route('/add')
def add():
    return redirect('/')


@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

@app.route('/add2')
def add2():
    session['x'] += 1
    return redirect('/')

@app.route('/add-custom', methods=['POST'])
def add_custom():
    count = request.form['custom']
    num = int(count)
    session['custom'] = num
    print(type(session['custom']))
    session['x'] += session['custom']
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
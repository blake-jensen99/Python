from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if not 'rndm' in session:
        import random
        session['rndm'] = random.randint(1,100)
    print(session['rndm'])


    if not 'guess' in session:
        high = 'none'
        low = 'none'
        correct = 'none'
    else:
        if session['guess'] < session['rndm']:
            high = 'none'
            low = "flex"
            correct = 'none'
        elif session['guess'] > session['rndm']:
            high = 'flex'
            low = 'none'
            correct = 'none'
        else:
            high = 'none'
            low = 'none'
            correct = 'flex'
    return render_template("index.html", high = high, low = low, correct = correct)


@app.route('/play', methods=['POST'])
def play():
    count = request.form['guess']
    num = int(count)
    session['guess'] = num
    print(session['guess'])
    
    return redirect('/')


@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
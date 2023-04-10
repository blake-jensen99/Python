from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if not 'x' in session:
        session['x'] = 0

    if not 'message' in session:
        session['message'] = ['Start']



    return render_template("index.html")






@app.route('/process_money', methods=['POST'])
def process_money():
    import random
    if request.form['form'] == 'farm':
        y = random.randint(10,20)
        session['message'].append(f'<li> Earned {{{y}}} gold from the farm! </li>')
    elif request.form['form'] == 'cave':
        y = random.randint(5,10)
        session['message'].append(f'<li> Earned {{{y}}} gold from the cave! </li>')
    elif request.form['form'] == 'house':
        y = random.randint(2,5)
        session['message'].append(f'<li> Earned {{{y}}} gold from the house! </li>')
    else:
        y = random.randint(-50,50)
        if y < 0:
            session['message'].append(f'<li> Lost {{{y+(-y)+(-y)}}} gold at the casino! </li>')
        else:
            session['message'].append(f'<li> Earned {{{y}}} gold from the casino! </li>')

    num = int(y)
    session['num'] = num
    session['x'] += session['num']
    return redirect('/')



@app.route('/clear')
def clear():
    session.clear()
    return redirect("/")





if __name__=="__main__":
    app.run(debug=True)
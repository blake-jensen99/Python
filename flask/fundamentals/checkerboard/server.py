from flask import Flask, render_template
app = Flask(__name__)

@app.route('/checker')
def index():
    return render_template("index.html", num = 8, num2 = 8, col = 'red', col2 = 'black' )	


@app.route('/checker/<int:num>')
def index2(num):
    return render_template("index.html", num = num, num2 = num, col = 'red', col2 = 'black')	


@app.route('/checker/<int:num>/<int:num2>')
def index3(num, num2):
    return render_template("index.html", num = num, num2 = num2, col = 'red', col2 = 'black')	


@app.route('/checker/<int:num>/<int:num2>/<string:col>')
def index4(num, num2,col):
    return render_template("index.html", num = num, num2 = num2, col = col, col2 = 'black')	


@app.route('/checker/<int:num>/<int:num2>/<string:col>/<string:col2>')
def index5(num, num2,col, col2):
    return render_template("index.html", num = num, num2 = num2, col = col, col2 = col2)	


@app.route('/checker/<string:col>')
def index6(col):
    return render_template("index.html", num = 8, num2 = 8, col = col, col2 = 'black')	

@app.route('/checker/<string:col>/<string:col2>')
def index7(col, col2):
    return render_template("index.html", num = 8, num2 = 8, col = col, col2 = col2)	



if __name__=="__main__":
    app.run(debug=True)
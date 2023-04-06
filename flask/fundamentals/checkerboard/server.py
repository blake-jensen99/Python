from flask import Flask, render_template
app = Flask(__name__)

@app.route('/checker')
def index():
    return render_template("index.html", num = 8)	


@app.route('/checker/<int:num>')
def index2(num):
    return render_template("index.html", num = num)	


@app.route('/checker/<int:num>/<int:num2>')
def index3(num, num2):
    return render_template("index3.html", num = num, num2 = num2)	


@app.route('/checker/<int:num>/<int:num2>/<string:col>')
def index4(num, num2,col):
    return render_template("index4.html", num = num, num2 = num2, col = col)	


@app.route('/checker/<int:num>/<int:num2>/<string:col>/<string:col2>')
def index5(num, num2,col, col2):
    return render_template("index5.html", num = num, num2 = num2, col = col, col2 = col2)	



if __name__=="__main__":
    app.run(debug=True)
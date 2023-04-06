from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:word>')
def say_hi(word):
    return f"Hi {word}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeating(num, word):
    return word * num



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)   
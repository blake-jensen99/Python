from flask import Flask

app = Flask(__name__)

DB = 'users'

app.secret_key = "secret"
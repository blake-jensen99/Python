from flask import Flask

app = Flask(__name__)

DB = 'email_schema'

app.secret_key = "secret"
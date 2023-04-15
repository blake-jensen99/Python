from flask import Flask

app = Flask(__name__)

DB = 'dojo_survey_schema'

app.secret_key = 'keep it secret, keep it safe'
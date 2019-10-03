import os
from app import app
from app import script
from flask import render_template, send_from_directory

@app.route('/<id>')
@app.route('/result/<id>')
def index(id):
    response = script.do(id)
    return render_template('index.html', title=response[0], content = response[1], url = response[2])

@app.route('/favicon.ico')
def favicon():
    return ""

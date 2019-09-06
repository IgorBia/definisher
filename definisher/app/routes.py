import os
from app import app
from app import script
from flask import render_template, send_from_directory

@app.route('/<id>')
@app.route('/result/<id>')
def index(id):
    response = script.do(id)
    content = response[0].decode().split("SplittingSentense")
    url = response[1]
    return render_template('index.html', title=content[0], content = content[1], url = url)

@app.route('/favicon.ico')
def favicon():
    return ""
    

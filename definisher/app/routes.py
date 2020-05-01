import os
from app import app
from app import script
from flask import render_template, send_from_directory

categories = ["Mathematics", "History", "Physics"]

@app.route('/')
def home():
    response = script.do()
    return render_template('state1.html', title=response[0], content = response[1], url = response[2], id = id)

@app.route('/result/<id>')
def index(id):
    if id in categories:
        response = script.do(id)
        return render_template('state1.html', title=response[0], content = response[1], url = response[2], id = id)
    else:
        return "<h1>Error 001 Category not find</h1>"

@app.route('/favicon.ico')
@app.route('/result/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

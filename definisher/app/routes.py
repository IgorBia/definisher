from app import app
from app import script
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    content = script.do().decode().split("SplittingSentense")
    return render_template('index.html', title=content[0], content = content[1])
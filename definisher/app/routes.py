from app import app
from app import script
from flask import render_template

@app.route('/')
def aaa():
    return render_template('state1.html')
@app.route('/index')
def index():
    content = script.do().decode().split("SplittingSentense")
    return render_template('base.html', title=content[0], content = content[1])
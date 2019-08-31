from app import app
from app import script
from flask import render_template

@app.route('/')
@app.route('/result')
def index():
    response = script.do()
    print(response)
    content = response[0].decode().split("SplittingSentense")
    url = response[1]
    return render_template('index.html', title=content[0], content = content[1], url = url)

@app.route('/favicon.ico')
def favicon():
    return 0

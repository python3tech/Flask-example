from flask import render_template

from app import app


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template('about-us.html')

@app.route('/signup',methods=['POST'])
def signup_function():
    payload = request.json

    pass

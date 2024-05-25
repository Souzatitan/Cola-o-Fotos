from flask import Flask, render_template

app=Flask(__name__)


@app.route('/home')
def home ():
    return render_template('templates\home.html')
@app.route('/cadastro')
def cadastro():
    pass
@app.route('/login')
def login():
    pass

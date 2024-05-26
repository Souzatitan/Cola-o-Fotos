from flask import Flask, render_template

app=Flask(__name__)


@app.route('/')
def home ():
    return render_template('home.html')
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
@app.route('/login')
def login():
    return render_template('login.html')

app.run(debug=True)
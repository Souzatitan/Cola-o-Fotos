from flask import Flask

app=Flask(__name__)


@app.route('/home')
def home ():
    pass
@app.route('/cadastro')
def cadastro():
    pass
@app.route('/login')
def login():
    pass

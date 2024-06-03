from flask import Flask, render_template

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('Login/login.html')
@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro/cadastro.html')
@app.route('/enviar')
def login():
    return render_template('Enviar/envia.html')
@app.route('/fotos')
def fotos():
    return render_template('Enviar/envia.html')



app.run(debug=True)
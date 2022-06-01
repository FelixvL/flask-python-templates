from flask import Flask
from flask import render_template

import voorbeeld

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Wereld!</p>"


@app.route("/anders")
def anders():
    voornaam = "felix"
    return "<p>Hello, Wereld! <br>Welkom "+voornaam+"</p>"

@app.route("/derde")
def derde():
    voornaam = "felix"
    return voorbeeld.vanmij()

@app.route("/vierde/<mijnvar>")
def vierde(mijnvar):
    return "dit is de var: "+mijnvar

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
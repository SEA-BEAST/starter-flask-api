from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/<name>/")
def error(name):
    return f"<h1>error</h1> <h4>this page has gone extinct. go back to the main website.</h4>"

if __name__ = "__main__":
    app.run(host="0.0.0.0", port=5000)

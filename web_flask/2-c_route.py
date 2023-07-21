#!/usr/bin/python3
"""script that starts a Flask web application:"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """the function to display hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello1():
    """changing route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_C(text):
    """displaying text"""
    return ("C " + text.replace("_", " "))


if __name__ == "__main__":
    app.run()

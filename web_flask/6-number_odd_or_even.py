#!/usr/bin/python3
"""script that starts a Flask web application:"""
from flask import Flask, render_template


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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python1(text="is cool"):
    """displaying text"""
    return ("Python " + text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number1(n):
    """displays number"""
    return str(n) + " is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def template1(n):
    """displays html page"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def template2(n):
    """displays html page"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run()
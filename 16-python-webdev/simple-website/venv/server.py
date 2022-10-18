from flask import Flask, render_template, url_for

app = Flask(__name__)


# Default home
@app.route("/index.html")
def my_home():
    return render_template("./index.html")


# Second home
@app.route("/")
def my_home2():
    return render_template("./index.html")


# About
@app.route("/about.html")
def about():
    return render_template("./about.html")


# Works
@app.route("/works.html")
def works():
    return render_template("./works.html")


# Works
@app.route("/work.html")
def work():
    return render_template("./work.html")


# Contact
@app.route("/contact.html")
def contact():
    return render_template("./contact.html")


# Components
@app.route("/components.html")
def components():
    return render_template("./components.html")

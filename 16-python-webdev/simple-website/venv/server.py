from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("./index.html")


@app.route("/blog")
def blog():
    return "<p>This is a blog</p>"


@app.route("/blog/2022/cats")
def cat_blog():
    return "<p>This is a cat blog</p>"

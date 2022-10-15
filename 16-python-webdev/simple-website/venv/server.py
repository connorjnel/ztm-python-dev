from flask import Flask, render_template, url_for

app = Flask(__name__)


# Default home
@app.route("/")
def home():
    return render_template("./index.html")


# Home with variable rules
# @app.route("/<username>/<int:post_id>")
# def hello_world(username=None, post_id=None):
#     return render_template("./index.html", name=username, post_id=post_id)


@app.route("/blog")
def blog():
    return "<p>This is a blog</p>"


@app.route("/blog/2022/cats")
def cat_blog():
    return "<p>This is a cat blog</p>"

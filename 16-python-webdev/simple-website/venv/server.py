from flask import Flask, render_template, url_for

app = Flask(__name__)


# Default home
@app.route("/")
def my_home():
    return render_template("./index.html")


# Links
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

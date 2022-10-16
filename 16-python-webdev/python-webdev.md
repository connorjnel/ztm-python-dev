# Python Web Dev

- Can use frozen flask to deploy site to netlify instead of normal flask

## Setting up flask

- Python has a http.server module, NOT recommended for production though as it has limited security
- Better solutions are Flask and Django
- Flask is smaller and lean, only has most needed items included
- Django is batteries included, comes with a ton of stuff built in
- With flask use virtual environment - start with `py -3 -m venv venv`
- Activate with `. activate` - run from scripts directory when using bash, otherwise use `source <venv>/bin/activate`

## Building a flask server

- Use pip freeze to generate requirements file for use with new environment, dont want to load a venv to repo as it likely wont work
- Folders need to be correct, if flask is in venv folder then make sure server.py is in venv folder
- Flask - Follow the quickstart guide for setting up basic server
- `flask --app server.py run` - Start server
- `export FLASK_APP=server.py` - set environment variable for server
- `flask run` - Run command once the envar has been set up
- `. activate` - run within venv/scripts to start virtual environment
- `deactivate` - exit virtual environment
- Enabling debug mode will auto restart server each time a code change occurs, good for dev, major security risk though so never on production
- Enable debug mode - `export FLASK_DEBUG=on`
- Creating route - `@app.route("/path")`
- Render html template - in func under path `return render_template("html")` - Need to place them in templates folder
- linking css and js files are more complicated than with normal html linking, place them in static folder, `static/style.css`, can also use django static method
- Favicon, can just link in html using `<link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}">`

## Jinja - Templating Engine

- For templating in py use Jinja - `pip install Jinja2`
- `{{}}` - Enclose some code to evaluate it as python, can insert into html docs when using flask
- `url_for` - Safer way to build urls, urls are dynamic
- variable rules - way to pass dynamic data into
- You can add variable sections to a URL by marking sections with `<variable_name>`. Your function then receives the `<variable_name>` as a keyword argument.

## MIME Type

- A MIME type is a label used to identify a type of data. It is used so software can know how to handle the data. It serves the same purpose on the Internet that file extensions do on Microsoft Windows.

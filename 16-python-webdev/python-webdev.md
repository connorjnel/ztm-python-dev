# Python Web Dev

- Tip - Can use frozen flask to deploy site to netlify instead of normal flask

## Setting up flask

- Python has a http.server module, NOT recommended for production though as it has limited security
- Better solutions are Flask and Django
- Flask is smaller and lean, only has most needed items included
- Django is batteries included, comes with a ton of stuff built in
- With flask use virtual environment - start with `py -3 -m venv venv`
- Activate with `. activate` - run from scripts directory when using bash, otherwise use `source <venv>/bin/activate`

## Building a flask server

- Tip - Use pip freeze to generate requirements file for use with new environment, dont want to load a venv to repo as it likely wont work
- Folders need to be correct, if flask is in venv folder then make sure server.py is in venv folder
- Flask - Follow the quickstart guide for setting up basic server
- `flask --app server.py run` - Start server
- `export FLASK_APP=server.py` - set environment variable for server
- `flask run` - Run command once the envar has been set up
- `deactivate` - exit virtual environment

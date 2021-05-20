from flask import Blueprint

app_default = Blueprint("default", __name__)


@app_default.route('/default')
def hello_world():
    return 'Hello World!'

from flask import Flask, jsonify
from flask import request
from flask import render_template
from flask import send_from_directory
import requests
import json
import logging


app = Flask(__name__)

log = logging.getLogger("webapp")

@app.before_first_request
def setup_logging():
    if not app.debug:
        # In production mode, add log handler to sys.stderr.
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)

@app.route('/js/<path:path>')
def send_js(path):
    app.logger.error("Serving " + str(path))
    return send_from_directory('js', path)


@app.route('/hello')
def hello_text():
    response = {}
    response['text'] = "Hello from python backend"
    return json.dumps(response)

@app.route("/")
def index_html():
    try:
      return render_template('index.html')
    except Exception as e:
      return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

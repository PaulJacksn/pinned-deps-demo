import requests
import urllib3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, dependencies!"
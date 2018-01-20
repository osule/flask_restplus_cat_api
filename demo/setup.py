from flask import Flask
from flask_pymongo import PyMongo

import demo

app = Flask('demo')
demo.db = PyMongo(app)
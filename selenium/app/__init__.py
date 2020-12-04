from flask import Flask
from flask_caching import Cache

import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
cache = Cache(app, config={"CACHE_TYPE": "simple"})
cache.init_app(app)

from app import routes
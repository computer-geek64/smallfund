#!/usr/bin/python3 -B
# api.py

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask
from flask_cors import CORS
from config import IP, PORT
from upload_blueprint import upload_blueprint
from products_blueprint import products_blueprint


app = Flask(__name__)
app.register_blueprint(upload_blueprint)
app.register_blueprint(products_blueprint)
CORS(app)


@app.route('/', methods=['GET'])
def get_home():
    return 'Hello, world!', 200


if __name__ == '__main__':
    app.run(IP, PORT)

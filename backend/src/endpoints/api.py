#!/usr/bin/python3 -B
# api.py

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask
from flask_cors import CORS
from config import IP, PORT


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def get_home():
    return 'Hello, world!', 200


if __name__ == '__main__':
    app.run(IP, PORT)

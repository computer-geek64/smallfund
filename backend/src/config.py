#!/usr/bin/python3 -B
# config.py

import os


if __name__ == '__main__':
    exit(0)


# Flask Server
IP = '0.0.0.0'
PORT = int(os.environ['PORT'])

# MySQL GCP Database
DB_HOST = 'localhost'
DB_NAME = 'hackgt8'
DB_USERNAME = os.environ['DB_USERNAME']
DB_PASSWORD = os.environ['DB_PASSWORD']

# Image options
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'svg', 'gif', 'bmp'}
UPLOAD_DIRECTORY = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'images')

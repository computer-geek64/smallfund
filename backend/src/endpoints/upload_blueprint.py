#!/usr/bin/python3
# upload_blueprint.py

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'util'))
import db
from auth import hash_password
from flask import Blueprint, request
from werkzeug.utils import secure_filename
from config import ALLOWED_EXTENSIONS, UPLOAD_DIRECTORY
from


upload_blueprint = Blueprint('upload_blueprint', __name__)


def allowed_filename(filename):
    if '.' not in filename:
        return False

    if filename.rsplit('.', 1)[1] not in ALLOWED_EXTENSIONS:
        return False

    return True


@upload_blueprint.route('/upload', methods=['POST'])
def post_upload():
    if 'name' not in request.form or 'description' not in request.form or 'price' not in request.form or 'image' not in request.files:
        return 'Bad request', 400

    seller_id = 1
    db.cursor.execute('''SELECT name FROM seller WHERE id = %s;''', (seller_id,))
    seller_name = db.cursor.fetchall()[0][0]

    name = request.form['name']
    description = request.form['description']
    price = float(request.form['price'])

    file = request.files['image']
    filename = secure_filename(file.filename.lower())

    if not allowed_filename(filename):
        return 'Invalid image', 400

    if not os.path.isdir(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)

    c

    filename = 'id' + '.' + filename.rsplit('.', 1)[1]
    file.save(os.path.join(UPLOAD_DIRECTORY, filename))
    return 'Success', 200

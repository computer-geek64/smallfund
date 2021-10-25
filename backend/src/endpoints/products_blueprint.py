#!/usr/bin/python3 -B
# products_blueprint.py

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'util'))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'util', 'api'))
import db
from config import UPLOAD_DIRECTORY
from ncr_api import list_of_objects, get_item
from flask import Blueprint, request, jsonify, send_from_directory


products_blueprint = Blueprint('products_blueprint', __name__)


@products_blueprint.route('/products', methods=['GET'])
def get_products():
    products = list_of_objects()
    for i in range(len(products)):
        products[i]['image'] = db.get_image(db.conn, db.cursor, int(products[i]['id']))
    return jsonify(products), 200


@products_blueprint.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    name, description, price = get_item(str(id))
    product = {
        'name': name,
        'description': description,
        'price': price,
        'image': db.get_image(db.conn, db.cursor, id)
    }

    return jsonify(product), 200


@products_blueprint.route('/image/<string:filename>', methods=['GET'])
def get_image(filename):
    return send_from_directory(UPLOAD_DIRECTORY, filename), 200

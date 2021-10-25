#!/usr/bin/python3 -B
# __init__.py

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import mysql.connector
from .schema import recreate as recreate_schema
from .seller import create as create_seller
from .product import create as create_product, get_image, search, delete as delete_product
from config import DB_HOST, DB_NAME, DB_USERNAME, DB_PASSWORD


conn = mysql.connector.connect(host=DB_HOST, database=DB_NAME, user=DB_USERNAME, password=DB_PASSWORD)
cursor = conn.cursor()

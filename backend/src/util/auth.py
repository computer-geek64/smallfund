#!/usr/bin/python3 -B
# auth.py

import hashlib


def hash_password(password):
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), 'salty'.encode('utf-8'), 100000).hex()

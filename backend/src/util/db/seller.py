#!/usr/bin/python3 -B
# seller.py

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from auth import hash_password


def create(conn, cursor, id, username, password):
    cursor.execute('''
INSERT INTO seller (
                id,
                name,
                password_hash
            )
     VALUES (
                %s,
                %s,
                %s
            )
''', (id, username, hash_password(password)))
    conn.commit()

#!/usr/bin/python3 -B
# schema.py

import os


def recreate(conn, cursor):
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'db', 'schema.sql'), 'r') as file:
        cursor.execute(file.read(), multi=True)

    conn.commit()

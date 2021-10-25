#!/usr/bin/python3 -B
# product.py


def create(conn, cursor, name, seller, image_filename):
    cursor.execute('''
INSERT INTO product (
                name,
                seller,
                image
            )
     VALUES (
                %s,
                %s,
                %s
            );
''', (name, seller, image_filename))
    conn.commit()


def get_image(conn, cursor, id):
    cursor.execute('''
SELECT image
  FROM product
 WHERE id = %s;
''', (id,))
    return cursor.fetchall()[0][0]


def search(conn, cursor, query):
    pass


def delete(conn, cursor, id):
    cursor.execute('''
DELETE FROM product
      WHERE id = %s;
''', (id,))
    conn.commit()

import sqlite3

def init_db():
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            price REAL,
            photo_id TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_product(name, description, price, photo_id):
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, description, price, photo_id) VALUES (?, ?, ?, ?)',
                   (name, description, price, photo_id))
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    conn.close()
    return rows
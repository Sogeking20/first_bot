import sqlite3

with sqlite3.connect('new_bot.db') as conn:
    cur = conn.cursor()


    cur.execute('''CREATE TABLE IF NOT EXISTS goods(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER,
                points INTEGER
    );''')
    conn.commit()


    cur.execute('INSERT INTO goods(chat_id, points) VALUES (?, ?)', [28347847, 10000])
    cur.execute('INSERT INTO goods(chat_id, points) VALUES (?, ?)', [28347847, 10000])
    conn.commit()




# cur.execute('INSERT INTO products(name, price, description) VALUES (?, ?, ?)', ['Гитара', 50000, 'Электрогитара премиум-класса'])
# conn.commit()

# cur.execute('INSERT INTO products(name, price, description) VALUES (?, ?, ?)', ['Барабан', 60000, 'Барабан премиум-класса'])
# conn.commit()

# cur.execute('SELECT name FROM products WHERE price < ?', [60000])
# result = cur.fetchall()

# print(result)
import sqlite3
import asyncio

connection = sqlite3.connect("initiate_db.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
)
''')


def get_all_products():
    cursor.execute("SELECT * FROM Products")
    all_products = cursor.fetchall()
    return all_products


allP = get_all_products()

# if __name__ == "__main__":
#     for i in range(1, 5):
#         cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                        (f"Таблеточка{i}", f"описание таблеточки{i}", i * 100))
#     allP = get_all_products()
#     print(allP)

connection.commit()
connection.close()

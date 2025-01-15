import sqlite3

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

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER NOT NULL,
balance INTEGER NOT NULL
)
''')


def get_all_products():
    all_products = cursor.execute("SELECT * FROM Products").fetchall()
    connection.commit()
    return all_products


# allP = get_all_products()


def get_all_users():
    all_users = cursor.execute("SELECT * FROM Users").fetchall()
    connection.commit()
    return all_users


# allU = get_all_users()


def add_user(username, email, age):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (username, email, age, 1000))
    connection.commit()


def is_included(username):
    userTrue = cursor.execute("SELECT username FROM Users WHERE username == ?", (username,)).fetchone()
    connection.commit()
    if userTrue:
        return True
    else:
        return False


# if __name__ == "__main__":
#     # for i in range(1, 5):
#     #     cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#     #                    (f"Таблеточка{i}", f"описание таблеточки{i}", i * 100))
#     # cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#     #                ("admin1", "admin1@mail.ru", 22, 1000000))
#     print(allP)
#     print(allU)
#     print(is_included("admin1"))

connection.commit()

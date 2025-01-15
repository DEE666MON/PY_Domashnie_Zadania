import sqlite3
# SELECT FROM WHERE GROUP BY HAVING ORDER BY

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"user{i}", f"example{i}@gmail.com", i*10, 1000))

# for i in range(1, 11, 2):
#     cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"user{i}"))

# for i in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users WHERE username = ?", (f"user{i}",))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
users = cursor.fetchall()
for username, email, age, balance in users:
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

connection.commit()
connection.close()

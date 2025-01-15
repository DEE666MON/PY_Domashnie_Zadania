import sqlite3

# SELECT FROM WHERE GROUP BY HAVING ORDER BY
# Функции: COUNT SUM AVG MIN MAX

connection = sqlite3.connect("not_telegram.db")
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

# cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
# users = cursor.fetchall()
# for username, email, age, balance in users:
#     print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

# cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
if (all_balances is not None and total_users != 0):
    print(all_balances / total_users)

connection.commit()
connection.close()

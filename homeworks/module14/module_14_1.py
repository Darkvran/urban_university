import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# for i in range(10):
#    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i+1}", f"example{i+1}@gmail.com", (i+1)*10, 1000))
#
# for i in range(10):
#     if i % 2 == 0:
#         cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500,f"User{i+1}"))
#
# for i in range(10):
#     if i % 3 == 0:
#         cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i+1}",))z
cursor.execute("SELECT username, email, age, balance from Users WHERE age != ?", (60,))
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")
connection.commit()
connection.close()
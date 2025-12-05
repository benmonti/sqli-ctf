import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE flag (
    value TEXT
)
""")

cursor.execute("INSERT INTO users VALUES (NULL, 'guest', 'guest123')")
cursor.execute("INSERT INTO flag VALUES ('flag{}')")

conn.commit()
conn.close()

print("Database created.")
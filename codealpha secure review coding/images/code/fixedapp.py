import sqlite3
import bcrypt

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE username = ?",
        (username,)
    )

    result = cursor.fetchone()
    conn.close()

    if result and bcrypt.checkpw(password.encode(), result[0]):
        return "Login successful"
    else:
        return "Login failed"

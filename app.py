
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = "users.db"


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)

        count = conn.execute(
            "SELECT COUNT(*) FROM users"
        ).fetchone()[0]

        if count == 0:
            conn.executemany(
                "INSERT INTO users (username, email) VALUES (?, ?)",
                [
                    ("alice", "alice@example.test"),
                    ("bob", "bob@example.test"),
                    ("charlie", "charlie@example.test"),
                ],
            )


@app.route("/")
def home():
    return (
        "Local SQL injection training lab. "
        "Use /search?username=alice"
    )



@app.route("/search")
def search():
    username = request.args.get("username", "")

    query = """
        SELECT id, username, email
        FROM users
        WHERE username = ?
    """

    with sqlite3.connect(DB_NAME) as conn:
        rows = conn.execute(query, (username,)).fetchall()

    return jsonify([
        {"id": row[0], "username": row[1], "email": row[2]}
        for row in rows
    ])

if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5001, debug=False)

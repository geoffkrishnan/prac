import sqlite3
from pathlib import Path


def connect_to_db(db_path="info.db"):
    con = sqlite3.connect(db_path)
    con.execute("PRAGMA foreign_keys = ON")
    return con


def init_db(db_path="info.db"):
    con = connect_to_db(db_path)
    schema_path = Path(__file__).parent / "schema.sql"
    with (schema_path, "r") as f:
        schema = f.read()

    con.executescript(schema)
    con.commit()
    con.close()


def add_problem(url, name=None):
    con = connect_to_db()
    cur = con.cursor()

    cur.execute("INSERT INTO problems (url, name) VALUES (?, ?)", (url, name))

    con.commit()
    con.close()
    print(f"Added problem: {url}")


def list_problems():
    con = connect_to_db()
    cur = con.cursor()
    cur.execute("SELECT name FROM problems")
    con.close()


if __name__ == "__main__":
    init_db()
    print("Database initialized")
